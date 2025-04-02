import requests
import os
import re
from pathlib import Path
from xml.sax.saxutils import escape

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

    mashup_lines.append(f'url = "{url}",')
    mashup_lines.append(f'response = Web.Contents(url, [Headers = [Authorization = "{API_TOKEN}"]]),')
    mashup_lines.append('json = Json.Document(response)')
    mashup_lines.append('in json')

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

# === Main Process ===
def generate_all_odc_files():
    print("Fetching Swagger spec...")
    res = requests.get(SWAGGER_URL)
    spec = res.json()

    for path, methods in spec["paths"].items():
        for method, details in methods.items():
            if method.lower() not in ["get", "post"]:  # limit to get for now
                continue

            tag = details.get("tags", ["General"])[0]
            op_id = details.get("operationId", f"{method}_{path.replace('/', '_')}")
            clean_name = re.sub(r'\W+', '_', op_id)

            params = [p["name"] for p in details.get("parameters", []) if p.get("in") == "path"]
            param_names = [p[0].upper() + p[1:] + "ID" if p.lower() == "id" else p[0].upper() + p[1:] for p in params]

            url = "https://jgiquality.qualer.com" + path
            generate_odc_file(tag, clean_name, url, param_names)

    print("ODC files generated in:", OUTPUT_DIR)

if __name__ == "__main__":
    generate_all_odc_files()
