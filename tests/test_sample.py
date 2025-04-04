import json
from pathlib import Path
from src.generate import generate_mashup_formula  # adjust if it’s in a subpackage
import pytest
from xml.etree import ElementTree as ET
import html

def load_expected_xml(filename):
    xml_text = (Path(__file__).parent / "test_files" / filename).read_text(encoding="utf-8")
    inner = xml_text.replace("<odc:PowerQueryMashupData>", "").replace("</odc:PowerQueryMashupData>", "").strip()
    unescaped = html.unescape(inner)
    root = ET.fromstring(unescaped)
    formula_node = root.find(".//{http://schemas.microsoft.com/DataMashup}Formula")
    return formula_node.text.strip()

def load_json(filename):
    with open(Path(__file__).parent / "test_files" / filename, encoding="utf-8") as f:
        return json.load(f)

def load_expected(filename):
    return (Path(__file__).parent / "test_files" / filename).read_text(encoding="utf-8").strip()
@pytest.mark.parametrize(
    "json_file, expected_m_file, expected_xml_file",
    [
        ('GetWorkOrders.json','expected_GetWorkOrders.m','expected_GetWorkOrders.xml'),
        ("no_params.json", "expected_no_params.m", "expected_no_params.xml"),
        ("path_params.json", "expected_path_params.m", "expected_path_params.xml"),
        ("query_params.json", "expected_query_params.m", "expected_query_params.xml"),
        ("both_types.json", "expected_both_types.m", "expected_both_types.xml"),
    ],
)
def test_mashup_generation(json_file, expected_m_file, expected_xml_file):
    """
    Test the mashup generation against both .m and embedded XML content.
    """
    ep = load_json(json_file)
    got = generate_mashup_formula(ep).strip()

    expected_m = load_expected(expected_m_file)
    assert got == expected_m, (
        f"\n--- Mismatch in M file for {json_file} ---\n"
        f"Expected:\n{expected_m}\n\nGot:\n{got}\n"
    )

    expected_xml = load_expected_xml(expected_xml_file)
    assert got == expected_xml, (
        f"\n--- Mismatch in XML for {json_file} ---\n"
        f"Expected:\n{expected_xml}\n\nGot:\n{got}\n"
    )