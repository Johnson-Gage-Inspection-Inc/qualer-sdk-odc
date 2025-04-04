import json
from pathlib import Path
from src.generate import generate_mashup_formula  # adjust if it’s in a subpackage
import pytest

def load_json(filename):
    with open(Path(__file__).parent / "test_files" / filename, encoding="utf-8") as f:
        return json.load(f)

def load_expected(filename):
    return (Path(__file__).parent / "test_files" / filename).read_text(encoding="utf-8").strip()
@pytest.mark.parametrize(
    "json_file, expected_file",
    [
        ("no_params.json", "expected_no_params.m"),
        ("path_params.json", "expected_path_params.m"),
        ("query_params.json", "expected_query_params.m"),
        ("both_types.json", "expected_both_types.m"),
    ],
)
def test_mashup_generation(json_file, expected_file):
    """
    Test the mashup generation function against known outputs.
    """
    ep = load_json(json_file)
    expected = load_expected(expected_file)
    got = generate_mashup_formula(ep).strip()

    assert got == expected, (
        f"\n--- Mismatch in {json_file} ---\n"
        f"Expected:\n{expected}\n\nGot:\n{got}\n"
    )
