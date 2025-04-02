import re
from pathlib import Path
import json 

def generate_markdown_files(spec: dict, docs_dir="Excel-Qualer-SDK/docs"):
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
`Excel-Qualer-SDK/{tag}/{clean_name}.odc`
"""

            file_path = docs_path / f"{clean_name}.md"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(markdown)


if __name__ == "__main__":
    with open("spec.json", "r", encoding="utf-8") as f:
        spec_raw = f.read()
    spec = json.loads(spec_raw)

    generate_markdown_files(spec)