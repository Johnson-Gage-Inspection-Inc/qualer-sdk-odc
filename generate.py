# flake8: noqa: E501
import json
import re
from pathlib import Path
from collections import defaultdict

# === Config ===
SWAGGER_URL = "https://jgiquality.qualer.com/swagger/docs/v1"
API_TOKEN = 'bf407589-f463-4046-ba2c-30642bd5d637'
OUTPUT_DIR = Path("Excel-Qualer-SDK")
BASE_URL = "https://jgiquality.qualer.com"


# === Template Generator ===
def generate_odc_file(ep):
    name = ep["clean_name"]
    (url,) = ep["url"],

    mashup_lines = []

    for parameter in ep["param_names"]:
        mashup_lines += [
            parameter,
            ' = Excel.CurrentWorkbook(){{[Name="',
            parameter,
            '"]}}[Content]{{0}}[Column1],'
        ]
        pattern = re.compile(rf"\{{{parameter}\}}", re.IGNORECASE)
        url = pattern.sub(f'" & Text.From({parameter}) & "', url)

    relative_url = url.replace(BASE_URL, "").lstrip("/")

    mashup_lines += [
        f'baseUrl = "{BASE_URL}",',
        f'relativeUrl = "{relative_url}",',
        "response = Web.Contents(",
        "    baseUrl,",
        "    [",
        '        RelativePath = Text.TrimStart(relativeUrl, "/"),',
        f'        Headers = [ Authorization = "Api-Token {API_TOKEN}" ]',
        "    ]",
        "),",
        "json = Json.Document(response),",
        "ConvertToTable = Table.FromList(json, Splitter.SplitByNothing(), null, null, ExtraValues.Error)",
        "in ConvertToTable",
    ]

    mashup_formula = "let\n    " + "\n    ".join(mashup_lines)

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

def yield_get_endpoints():
    with open("spec.json", encoding="utf-8") as f:
        spec = json.load(f)
    for path, methods in spec["paths"].items():
        for method, details in methods.items():
            if method.lower() != "get":
                continue

            tag = details.get("tags", ["General"])[0]
            op_id = details.get("operationId", f"{method}_{path.replace('/', '_')}")
            clean_name = re.sub(r"\W+", "_", op_id)
            params = [
                p["name"]
                for p in details.get("parameters", [])
                if p.get("in") == "path"
            ]
            param_names = [
                p[0].upper() + p[1:] + "ID" if p.lower() == "id" else p[0].upper() + p[1:]
                for p in params
            ]
            url = "https://jgiquality.qualer.com" + path

            yield {
                "tag": tag,
                "path": path,
                "method": method,
                "details": details,
                "clean_name": clean_name,
                "op_id": op_id,
                "url": url,
                "params": params,
                "param_names": param_names,
            }


def generate_markdown_file(docs_path, ep):
    pram_doc = "\n".join([f"- `{p}` (path)" for p in ep["params"]]) or "None"
    range_doc = "\n".join([f"- `{r}`" for r in ep["param_names"]]) or "None"
    desc = ep["details"].get("description", "No description provided.").strip()

    markdown = f"""# `{ep['clean_name']}`

**URL Template:**
`GET {ep['path']}`

**Parameters:**
{pram_doc}

**Excel Named Range(s):**
{range_doc}

**Description:**
{desc}

**Group (Tag):**
{ep['tag']}

**ODC File:**
[Excel-Qualer-SDK/{ep['tag']}/{ep['clean_name']}.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/{ep['tag']}/{ep['clean_name']}.odc)

---

To Use in Excel:
---

1. Go to the ![`Data`](https://github.com/user-attachments/assets/da437a70-57b3-4c5b-bb01-4910ece19ed1)
 tab.
3. Click ![Existing Connections](https://github.com/user-attachments/assets/a2f1ed67-b2e0-4c23-ac90-68c870e60289)
4. Click ![`Browse for More...`](https://github.com/user-attachments/assets/8e698494-6865-41e7-b6fa-043aea81809a)
5. Paste the following into the URL bar
```
\\\\jgiquality.sharepoint.com@SSL\\sites\\JGI\\Shared Documents\\General\\Excel-Qualer-SDK\\{ep['tag']}\\
```

![image](https://github.com/user-attachments/assets/1e1a8d87-0377-446d-aaf5-d78562991db3)

6. Select `{ep['clean_name']}.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
"""

    file_path = docs_path / f"{ep['clean_name']}.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(markdown)


# === Main Process ===
def generate_all_odc_files():
    docs_path = Path(docs_dir)
    docs_path.mkdir(parents=True, exist_ok=True)

    for ep in yield_get_endpoints():
        generate_markdown_file(docs_path, ep)
        generate_odc_file(ep)
    print("ODC files generated in:", OUTPUT_DIR)


def generate_docs_index(docs_dir="docs"):
    docs_path = Path(docs_dir)
    index_file = docs_path / "README.md"

    # Group docs by prefix (tag)
    groups = defaultdict(list)
    markdown_files = docs_path.glob("*.md")
    for doc in sorted(p for p in markdown_files if p.name != "README.md"):
        parts = doc.stem.split("_", 1)
        if len(parts) == 2:
            tag, rest = parts
        else:
            tag, rest = "General", parts[0]
        groups[tag].append((doc.name, rest.replace("_", " ")))

    with open(index_file, "w", encoding="utf-8") as f:
        f.write("# 📖 Qualer API Documentation Index\n\n")
        f.write("This index lists all `GET` endpoints, grouped by tag.\n\n")

        for tag in sorted(groups):
            f.write(f"## {tag}\n\n")
            for filename, label in sorted(groups[tag]):
                f.write(f"- [{label}](./{filename})\n")
            f.write("\n")


if __name__ == "__main__":
    docs_dir = "docs"
    generate_all_odc_files()
    print("ODC files generated in:", OUTPUT_DIR)
    print("Markdown files generated in:", docs_dir)
    generate_docs_index(docs_dir)
    print("Markdown index generated in:", docs_dir)
