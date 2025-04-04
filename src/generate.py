# flake8: noqa: E501
from pathlib import Path
from src.doc_writer import generate_markdown_file, generate_docs_index
from src.odc_writer import render_odc_xml
import json
import re

# === Config ===
SWAGGER_URL = "https://jgiquality.qualer.com/swagger/docs/v1"
API_TOKEN = 'bf407589-f463-4046-ba2c-30642bd5d637'
OUTPUT_DIR = Path("Excel-Qualer-SDK")
BASE_URL = "https://jgiquality.qualer.com"

def normalize_name(n): return n.replace(".", "_")


# === Template Generator ===
def generate_odc_file(ep):
    name = ep["clean_name"]
    url = ep["url"]

    mashup_lines = []
    for param in ep['path_params'] + ep['query_params']:
        mashup_lines.append(
            f'{param} = try Excel.CurrentWorkbook(){{'
            f'[Name="{param}"]}}[Content]{{0}} otherwise "",'
        )

    for param in ep['path_params']:
        pattern = re.compile(rf"\{{{param}\}}", re.IGNORECASE)
        url = pattern.sub(f'" & Text.From({param}) & "', url)

    query_option_lines = []
    combine_names = []


    if ep['query_params']:
        names = [p["name"] for p in ep["params"] if p["in"] == "query"]
        for i, p in enumerate(names):
            varname = f"q{i+1}"
            query_option_lines.append(
                f'{varname} = if Text.Length({p}) > 0 then [ {p} = {p} ] else [],'
            )
            combine_names.append(varname)

        query_option_lines.append(f'QueryOptions = Record.Combine({{{", ".join(combine_names)}}}),')
    else:
        query_option_lines.append('QueryOptions = [],')


    mashup_lines += query_option_lines + [
        f'baseUrl = "{BASE_URL}",',
        f'relativeUrl = "{ep["relative_url"]}",',
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

    mashup_formula = "let\n    " + "\n    ".join(mashup_lines)

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

def generate_mashup_formula(ep):
    def normalize_name(n): return n.replace(".", "_")

    path_param_pairs = zip(ep["path_params"], ep["excel_path_params"])
    query_param_pairs = zip(ep["query_params"], ep["excel_query_params"])

    lines = []

    # Declare all Excel-named params
    for _, excel in list(path_param_pairs) + list(query_param_pairs):
        safe_excel = normalize_name(excel)
        lines.append(
            f'{safe_excel} = try Excel.CurrentWorkbook(){{[Name="{excel}"]}}[Content]{{0}} otherwise "",'
        )

    # Restore zip since it’s been consumed
    path_param_pairs = zip(ep["path_params"], ep["excel_path_params"])

    # Replace placeholders in URL
    url = ep["relative_url"]
    for orig, excel in zip(ep["path_params"], ep["excel_path_params"]):
        safe_excel = normalize_name(excel)
        pattern = re.compile(rf"\{{{orig}\}}", re.IGNORECASE)
        url = pattern.sub(f'" & Text.From({safe_excel}) & "', url)

    # Build query param handling
    combine_names = []
    for i, (orig, excel) in enumerate(zip(ep["query_params"], ep["excel_query_params"])):
        safe_excel = normalize_name(excel)
        varname = f"q{i+1}"
        lines.append(
            f'{varname} = if Text.Length({safe_excel}) > 0 then [ "{orig}" = {safe_excel} ] else [],'
        )
        combine_names.append(varname)

    if combine_names:
        lines.append(f'QueryOptions = Record.Combine({{{", ".join(combine_names)}}}),')
    else:
        lines.append('QueryOptions = [],')

    # Core request logic
    lines += [
        f'baseUrl = "{BASE_URL}",',
        f'relativeUrl = "{url}",',
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
    ]

    return "let\n    " + "\n    ".join(lines) + "\nin " + lines[-1].split(" = ")[0]


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
