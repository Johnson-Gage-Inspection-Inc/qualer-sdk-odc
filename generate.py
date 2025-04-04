# flake8: noqa: E501
from doc_writer import generate_markdown_file, generate_docs_index
from pathlib import Path
import json
import re

# === Config ===
SWAGGER_URL = "https://jgiquality.qualer.com/swagger/docs/v1"
API_TOKEN = 'bf407589-f463-4046-ba2c-30642bd5d637'
OUTPUT_DIR = Path("Excel-Qualer-SDK")
BASE_URL = "https://jgiquality.qualer.com"


# === Template Generator ===
def generate_odc_file(ep):
    name = ep["clean_name"]
    (url,) = ep["url"],

    mashup_lines = ["let"]
    for param in ep['path_params'] + ep['query_params']:
        mashup_lines += [
            param,
            ' = Excel.CurrentWorkbook(){{[Name="',
            param,
            '"]}}[Content]{{0}}[Column1],'
            ]

    for param in ep['path_params']:
        pattern = re.compile(rf"\{{{param}\}}", re.IGNORECASE)
        url = pattern.sub(f'" & Text.From({param}) & "', url)

    query_options = 'QueryOptions = '
    if ep['query_params']:
        names = [p["name"] for p in ep["params"] if p["in"] == "query"]
        conds = [f'if Text.Length({p}) > 0 then [ {p} = {p} ] else []' for p in names]
        query_options += f'{" & ".join(conds)},'
    else:
        query_options += '[],'

    mashup_lines += [
        query_options,
        f'baseUrl = "{BASE_URL}",',
        f'relativeUrl = "{ep['relative_url']}",',
        "response = Web.Contents(",
        "    baseUrl,",
        "    [",
        '        RelativePath = Text.TrimStart(relativeUrl, "/"),',
        '        Query = QueryOptions,',
        f'        Headers = [ Authorization = "Api-Token {API_TOKEN}" ]',
        "    ]",
        "),",
        "json = Json.Document(response),",
        "ConvertToTable = Table.FromList(json, Splitter.SplitByNothing(), null, null, ExtraValues.Error)",
        "in ConvertToTable",
    ]

    mashup_formula = "\n    ".join(mashup_lines)

    odc_xml = (
        f"""<html xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns="http://www.w3.org/TR/REC-html40">

<head>
<meta http-equiv=Content-Type content="text/x-ms-odc; charset=utf-8">
<meta name=ProgId content=ODC.Database>
<meta name=SourceType content=OLEDB>
<title>{name}</title>
<xml id=docprops><o:DocumentProperties
  xmlns:o="urn:schemas-microsoft-com:office:office"
  xmlns="http://www.w3.org/TR/REC-html40">
  <o:Description>Connection to the '{name}' query in the workbook.</o:Description>
  <o:Name>{name}</o:Name>
 </o:DocumentProperties>
</xml><xml id=msodc><odc:OfficeDataConnection
  xmlns:odc="urn:schemas-microsoft-com:office:odc"
  xmlns="http://www.w3.org/TR/REC-html40">
  <odc:PowerQueryConnection odc:Type="OLEDB">
   <odc:ConnectionString>Provider=Microsoft.Mashup.OleDb.1;Data Source=$Workbook$;Location={name};Extended Properties=&quot;&quot;</odc:ConnectionString>
   <odc:CommandType>SQL</odc:CommandType>
   <odc:CommandText>SELECT * FROM [{name}]</odc:CommandText>
  </odc:PowerQueryConnection>
  <odc:PowerQueryMashupData>
    &lt;Mashup xmlns:xsd=&quot;http://www.w3.org/2001/XMLSchema&quot; xmlns:xsi=&quot;http://www.w3.org/2001/XMLSchema-instance&quot; xmlns=&quot;http://schemas.microsoft.com/DataMashup&quot;&gt;&lt;Client&gt;EXCEL&lt;/Client&gt;&lt;Version&gt;2.140.405.0&lt;/Version&gt;&lt;MinVersion&gt;2.21.0.0&lt;/MinVersion&gt;&lt;Culture&gt;en-US&lt;/Culture&gt;&lt;SafeCombine&gt;true&lt;/SafeCombine&gt;&lt;Items&gt;&lt;Query Name=&quot;{name}&quot;&gt;&lt;Formula&gt;&lt;![CDATA[{mashup_formula}]]&gt;&lt;/Formula&gt;&lt;IsParameterQuery xsi:nil=&quot;true&quot; /&gt;&lt;IsDirectQuery xsi:nil=&quot;true&quot; /&gt;&lt;/Query&gt;&lt;/Items&gt;&lt;/Mashup&gt;
 </odc:PowerQueryMashupData>
 </odc:OfficeDataConnection>
</xml>
"""
        + """
<style>
<!--
    .ODCDataSource
    {
    behavior: url(dataconn.htc);
    }
-->
</style>"""
    )

    folder = OUTPUT_DIR / ep["tag"]
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{name}.odc"
    with open(path, "w", encoding="utf-8") as f:
        f.write(odc_xml)
    return path

def yield_get_endpoints(spec):
    for path, methods in spec["paths"].items():
        for method, details in methods.items():
            if method.lower() != "get":
                continue

            tag = details.get("tags", ["General"])[0]
            op_id = details.get("operationId", f"{method}_{path.replace('/', '_')}")

            clean_name = re.sub(r'\\W+', '_', op_id)
            params = details.get("parameters", [])
            if required_params:= [p for p in params if p.get("required")]:
                p = required_params[0]["name"]
                clean_name += f"By{p[0].upper() + p[1:]}"
            param_names = [p["name"] for p in params]
            param_names = [
                p[0].upper() + p[1:] + "ID" if p.lower() == "id" else p[0].upper() + p[1:]
                for p in param_names
            ]
            path_params = [p["name"] for p in params if p["in"] == "path"]
            query_params = [p["name"] for p in params if p["in"] == "query"]
            excel_path_params = [p[0].upper() + p[1:] for p in path_params]
            excel_query_params = [p[0].upper() + p[1:] for p in query_params]
            url = "https://jgiquality.qualer.com" + path
            relative_url = url.replace(BASE_URL, "").lstrip("/")

            yield {
                "tag": tag,
                "path": path,
                "method": method,
                "details": details,
                "clean_name": clean_name,
                "op_id": op_id,
                "params": params,
                "param_names": param_names,
                "path_params": path_params,
                "query_params": query_params,
                "excel_path_params": excel_path_params,
                "excel_query_params": excel_query_params,
                "url": url,
                "relative_url": relative_url,
            }


if __name__ == "__main__":
    docs_dir = "docs"
    docs_path = Path(docs_dir)
    docs_path.mkdir(parents=True, exist_ok=True)

    with open("spec.json", encoding="utf-8") as f:
        spec = json.load(f)
    for ep in yield_get_endpoints(spec):
        generate_markdown_file(docs_path, ep, spec)
        generate_odc_file(ep)
    print("ODC files generated in:", OUTPUT_DIR)
    print("ODC files generated in:", OUTPUT_DIR)
    print("Markdown files generated in:", docs_dir)
    generate_docs_index(docs_dir)
    print("Markdown index generated in:", docs_dir)
