from pathlib import Path
from src.generate import generate_mashup_formula  # adjust if it’s in a subpackage
import json
import pytest
import re
import html


def load_expected_xml(file):
    path = Path("tests") / "test_files" / file
    return path.read_bytes().decode("utf-8")

def load_json(filename):
    with open(Path(__file__).parent / "test_files" / filename, encoding="utf-8") as f:
        return json.load(f)

def load_expected(filename):
    return (Path(__file__).parent / "test_files" / filename).read_text(encoding="utf-8").strip()


@pytest.mark.parametrize(
    "json_file, expected_xml_file",
    [
        ("GetWorkOrders.json", "expected_GetWorkOrders.xml"),
        ("no_params.json", "expected_no_params.xml"),
        ("path_params.json", "expected_path_params.xml"),
        ("query_params.json", "expected_query_params.xml"),
        ("both_types.json", "expected_both_types.xml"),
    ],
)
def test_mashup_generation(json_file, expected_xml_file):
    ep = load_json(json_file)
    got = generate_mashup_formula(ep).strip()

    expected_full = load_expected_xml(expected_xml_file)
    expected_unescaped = html.unescape(expected_full)

    m = re.search(r"<Formula><!\[CDATA\[(.*?)\]\]></Formula>", expected_unescaped, flags=re.DOTALL)
    assert m, f"No CDATA section found in: {expected_xml_file}"

    expected_cdata = m.group(1).strip()
    assert html.unescape(got) == expected_cdata, (
        f"\n--- Mismatch in XML for {json_file} ---\n"
        f"Expected:\n{expected_cdata}\n\nGot:\n{got}\n"
    )



@pytest.mark.parametrize(
    "json_file, expected_m_file",
    [
        ('GetWorkOrders.json','expected_GetWorkOrders.m'),
        ("no_params.json", "expected_no_params.m"),
        ("path_params.json", "expected_path_params.m"),
        ("query_params.json", "expected_query_params.m"),
        ("both_types.json", "expected_both_types.m"),
    ],
)
def test_m_generation(json_file, expected_m_file):
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