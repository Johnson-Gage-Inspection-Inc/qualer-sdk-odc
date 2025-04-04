from collections import defaultdict
from pathlib import Path
import pandas as pd

def generate_markdown_file(docs_path, ep, spec):
    pram_doc = ""
    for param in ep['params']:
        param_name = param["name"]
        param_type = param["type"]
        param_format = param.get("format", "string")
        pram_doc += '- *' if param['required'] else '- '
        pram_doc += f"`{param_name}`: `{param_type}`\n"

    # Format parameters list
    param_doc = ""
    for param in ep['params']:
        prefix = "- *" if param.get('required') else "- "
        param_doc += f"{prefix}`{param['name']}`: `{param['type']}`\n"

    # Named ranges
    range_doc = "\n".join([f"- `{r}`" for r in ep.get("param_names", [])]) or "None"

    # Description
    desc = ep["details"].get("description", "No description provided.").strip()

    # Resolve schema for 200 OK
    ok_response = ep['details']['responses']['200']['schema']
    flat_fields = flatten_properties(ok_response, spec)
    df = pd.DataFrame([
        {"Field": k, "Type": v}
        for k, v in flat_fields.items()
    ])
    response_schema_md = df.to_markdown(index=False, tablefmt="pipe")

    markdown = f"""# `{ep['clean_name']}`

**URL Template:**
`GET {ep['path']}`

**Parameters:**
{pram_doc}

> *Required parameters are marked with an asterisk (*).

**Excel Named Range(s):**
{range_doc}


**Description:**
{desc}

### Response Schema

#### OK [200]

{response_schema_md}

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

    doc_name = ep["clean_name"].replace(f"{ep['tag']}_", "")
    folder = docs_path / ep['tag']
    folder.mkdir(parents=True, exist_ok=True)
    file_path = folder / f"{doc_name}.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(markdown)

def resolve_schema(schema, spec):
    """
    Flattens a schema definition by following $refs iteratively.
    Returns either:
      - A dict of properties (for object types)
      - A string type (e.g., 'string', 'integer')
    """
    while True:
        # Handle arrays
        if schema.get("type") == "array":
            items = schema.get("items", {})
            if "$ref" in items:
                ref = items["$ref"].split("/")[-1]
                schema = spec["definitions"].get(ref, {})
            elif "type" in items:
                # Array of primitives
                return f"array of {items['type']}"
            else:
                raise ValueError(f"Unexpected array schema: {schema}")

        # Handle $ref
        elif "$ref" in schema:
            ref = schema["$ref"].split("/")[-1]
            schema = spec["definitions"].get(ref, {})

        # Handle plain types (end condition)
        elif "type" in schema:
            if schema["type"] == "object" and "properties" in schema:
                return schema["properties"]
            return schema["type"]

        else:
            raise ValueError(f"Unable to resolve schema: {schema}")


def flatten_properties(schema, spec, parent_key=""):
    flat_fields = {}

    if "$ref" in schema:
        ref = schema["$ref"].split("/")[-1]
        schema = spec["definitions"].get(ref, {})
        return flatten_properties(schema, spec, parent_key)

    if schema.get("type") == "array":
        items = schema.get("items", {})
        if "$ref" in items:
            ref = items["$ref"].split("/")[-1]
            nested_schema = spec["definitions"].get(ref, {})
            return flatten_properties(nested_schema, spec, parent_key)
        elif "type" in items:
            flat_fields[parent_key] = f"array of {items['type']}"
            return flat_fields
        else:
            flat_fields[parent_key] = "array"
            return flat_fields

    if schema.get("type") == "object" and "properties" in schema:
        for key, prop in schema["properties"].items():
            full_key = f"{parent_key}.{key}" if parent_key else key
            nested = flatten_properties(prop, spec, full_key)
            flat_fields.update(nested)
        return flat_fields

    if parent_key:
        flat_fields[parent_key] = schema.get("type", "unknown")
    return flat_fields


def generate_docs_index(docs_dir):
    docs_path = Path(docs_dir)
    index_file = docs_path / "README.md"

    groups = defaultdict(list)
    markdown_files = docs_path.rglob("*.md")
    for doc in sorted(p for p in markdown_files if p.name != "README.md"):
        parts = doc.stem.split("_", 1)
        if len(parts) == 2:
            tag, rest = parts
        else:
            tag, rest = "General", parts[0]
        groups[tag].append((doc.relative_to(docs_path), rest.replace("_", " ")))

    with open(index_file, "w", encoding="utf-8") as f:
        f.write("# 📖 Qualer API Documentation Index\n\n")
        f.write("This index lists all `GET` endpoints, grouped by tag.\n\n")

        for tag in sorted(groups):
            f.write(f"## {tag}\n\n")
            for path, label in sorted(groups[tag]):
                f.write(f"- [{label}]({path.as_posix()})\n")
            f.write("\n")
