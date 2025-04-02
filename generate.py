import json
import os
import re
from pathlib import Path
from collections import defaultdict

# === Config ===
SWAGGER_URL = "https://jgiquality.qualer.com/swagger/docs/v1"
API_TOKEN = os.getenv("QUALER_API_TOKEN")
OUTPUT_DIR = Path("Excel-Qualer-SDK")

# === Template Generator ===
def generate_odc_file(group, name, url, parameters):
    mashup_lines = []

    for param in parameters:
        mashup_lines.append(f'{param} = Excel.CurrentWorkbook(){{[Name="{param}"]}}[Content]{{0}}[Column1],')

    for param in parameters:
        url = url.replace(f"{{{param.lower()}}}", f'" & Text.From({param}) & "')

    base_url = "https://jgiquality.qualer.com"
    relative_url = url.replace(base_url, "").lstrip("/")

    mashup_lines += [
        f'baseUrl = "{base_url}",',
        f'relativeUrl = "{relative_url}",',
        'response = Web.Contents(',
        '    baseUrl,',
        '    [',
        '        RelativePath = Text.TrimStart(relativeUrl, "/"),',
        '        Headers = [ Authorization = "Api-Token bf407589-f463-4046-ba2c-30642bd5d637" ]',
        '    ]',
        '),',
        'json = Json.Document(response),',
        'ConvertToTable = Table.FromList(json, Splitter.SplitByNothing(), null, null, ExtraValues.Error)',
        'in ConvertToTable'
    ]

    mashup_formula = "let\n    " + "\n    ".join(mashup_lines)

    odc_xml = f"""<html xmlns:o="urn:schemas-microsoft-com:office:office"
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
""" + """
<style>
<!--
    .ODCDataSource
    {
    behavior: url(dataconn.htc);
    }
-->
</style>"""

    folder = OUTPUT_DIR / group
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{name}.odc"
    with open(path, "w", encoding="utf-8") as f:
        f.write(odc_xml)
    return path


def generate_markdown_files(spec: dict, docs_dir):
    docs_path = Path(docs_dir)
    docs_path.mkdir(parents=True, exist_ok=True)

    for path, methods in spec["paths"].items():
        for method, details in methods.items():
            if method.lower() != "get":
                continue

            tag = details.get("tags", ["General"])[0]
            op_id = details.get("operationId", f"{method}_{path.replace('/', '_')}")
            clean_name = re.sub(r'\W+', '_', op_id)

            parameters = [p["name"] for p in details.get("parameters", []) if p.get("in") == "path"]
            param_ranges = [p[0].upper() + p[1:] + "ID" if p.lower() == "id" else p[0].upper() + p[1:] for p in parameters]
            param_doc = "\n".join([f"- `{p}` (path)" for p in parameters]) or "None"
            range_doc = "\n".join([f"- `{r}`" for r in param_ranges]) or "None"
            desc = details.get("description", "No description provided.")

            markdown = f"""# `{clean_name}`

**URL Template:**  
`GET {path}`

**Parameters:**  
{param_doc}

**Excel Named Range(s):**  
{range_doc}

**Description:**  
{desc.strip()}

**Group (Tag):**  
{tag}

**ODC File:**  
`[Excel-Qualer-SDK/{tag}/{clean_name}.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/{tag}/{clean_name}.odc)`
"""

            file_path = docs_path / f"{clean_name}.md"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(markdown)

# === Main Process ===
def generate_all_odc_files(spec: dict):

    for path, methods in spec["paths"].items():
        for method, details in methods.items():
            if method.lower() != "get":  # limit to get for now
                continue

            tag = details.get("tags", ["General"])[0]
            op_id = details.get("operationId", f"{method}_{path.replace('/', '_')}")
            clean_name = re.sub(r'\W+', '_', op_id)

            params = [p["name"] for p in details.get("parameters", []) if p.get("in") == "path"]
            param_names = [p[0].upper() + p[1:] + "ID" if p.lower() == "id" else p[0].upper() + p[1:] for p in params]

            url = "https://jgiquality.qualer.com" + path
            generate_odc_file(tag, clean_name, url, param_names)

    print("ODC files generated in:", OUTPUT_DIR)

def generate_docs_index(docs_dir="docs"):
    docs_path = Path(docs_dir)
    index_file = docs_path / "README.md"

    # Group docs by prefix (tag)
    groups = defaultdict(list)
    for doc in sorted(p for p in docs_path.glob("*.md") if p.name != "README.md"):
        parts = doc.stem.split("_", 1)
        if len(parts) == 2:
            tag, rest = parts
        else:
            tag, rest = "General", parts[0]
        groups[tag].append((doc.name, rest.replace("_", " ")))

    with open(index_file, "w", encoding="utf-8") as f:
        f.write("# 📖 Qualer API Documentation Index\n\n")
        f.write("This index lists all documented `GET` endpoints, grouped by tag.\n\n")

        for tag in sorted(groups):
            f.write(f"## {tag}\n\n")
            for filename, label in sorted(groups[tag]):
                f.write(f"- [{label}](./{filename})\n")
            f.write("\n")

if __name__ == "__main__":
    with open("spec.json", encoding="utf-8") as f:
        spec = json.load(f)
    generate_all_odc_files(spec)
    print("ODC files generated in:", OUTPUT_DIR)
    docs_dir = "docs"
    generate_markdown_files(spec, docs_dir)
    print("Markdown files generated in:", docs_dir)
    generate_docs_index(docs_dir)
    print("Markdown index generated in:", docs_dir)