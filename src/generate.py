from pathlib import Path
from src.doc_writer import generate_markdown_file, generate_docs_index
from src.odc_writer import render_odc_xml
import json
import re

# === Config ===
SWAGGER_URL = "https://jgiquality.qualer.com/swagger/docs/v1"
OUTPUT_DIR = Path("Excel-Qualer-SDK")
BASE_URL = "https://jgiquality.qualer.com"


# === Template Generator ===
def generate_odc_file(ep):
    name = ep["clean_name"]
    mashup_formula = generate_mashup_formula(ep)
    odc_xml = render_odc_xml(name, mashup_formula)

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
            if required_params := [p for p in params if p.get("required")]:
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


def generate_mashup_formula(ep):
    def normalize_name(n):
        return n.replace(".", "_")

    # === Gather parameters with metadata
    required_path_params = []
    optional_query_params = []
    required_query_params = []

    for param in ep["params"]:
        pname = param["name"]
        excel = ep["excel_path_params"][ep["path_params"].index(pname)] if param["in"] == "path" else ep["excel_query_params"][ep["query_params"].index(pname)]
        safe_excel = normalize_name(excel)

        if param["in"] == "path":
            required_path_params.append((pname, excel, safe_excel))
        elif param["in"] == "query":
            if param.get("required", False):
                required_query_params.append((pname, excel, safe_excel))
            else:
                optional_query_params.append((pname, excel, safe_excel))

    lines = []

    # Path parameters: no try/otherwise
    for _, excel, safe_excel in required_path_params:
        lines.append(
            f'{safe_excel} = Text.From(Excel.CurrentWorkbook(){{[Name="{excel}"]}}[Content][Column1]{{0}}),'
        )

    # Query parameters: always wrapped in try
    for _, excel, safe_excel in required_query_params + optional_query_params:
        lines.append(
            f'{safe_excel} = try Text.From(Excel.CurrentWorkbook(){{[Name="{excel}"]}}[Content][Column1]{{0}}) otherwise "",'
        )

    combine_names = []
    for orig, excel, safe_excel in required_query_params + optional_query_params:
        varname = orig  # use actual parameter name
        lines.append(
            f'{varname} = if Text.Length({safe_excel}) > 0 then [ {orig} = {safe_excel} ] else [],'
        )
        combine_names.append(varname)

    # === Replace path placeholders in URL
    url = ep["relative_url"]
    for orig, excel, safe_excel in required_path_params:
        pattern = re.compile(rf"\{{{orig}\}}", re.IGNORECASE)
        url = pattern.sub(f'" & {safe_excel} & "', url)

    if combine_names:
        lines.append(f'QueryOptions = Record.Combine({{{", ".join(combine_names)}}}),')
    else:
        lines.append("QueryOptions = [],")

    # === Mashup logic
    lines += [
        f'baseUrl = "{BASE_URL}",',
        f'relativeUrl = "{url}",',
        'TokenText = Text.Trim(Text.FromBinary(',
        '    Web.Contents("https://jgiquality.sharepoint.com/sites/JGI/Shared%20Documents/General/apikey.txt")',
        ')),',
        "response = Web.Contents(",
        "    baseUrl,",
        "    [",
        '        RelativePath = Text.TrimStart(relativeUrl, "/"),',
        "        Query = QueryOptions,",
        '        Headers = [ Authorization = TokenText ]',
        "    ]",
        "),",
        "json = Json.Document(response),",
        'ConvertToTable = if Value.Is(json, type list) then Table.FromRecords(json) else Record.ToTable(json)',
    ]

    # === Final string
    br = '&#13;&#10;'  # XML-safe line break
    joined_lines = f"{br}    ".join(lines)
    resulting_table = lines[-1].split(" = ")[0]
    return (f"let{br}    {joined_lines}{br}in{br}    {resulting_table}").rstrip()


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
    print("Markdown files generated in:", docs_path)
    generate_docs_index(docs_path)
    print("Markdown index generated in:", docs_path)
