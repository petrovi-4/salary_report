import pytest

from reporting.parser import parse_csv, parse_files

CSV_CONTENT = """id,email,name,department,hours_worked,hourly_rate
1,alise@test.com,Alice,HR,160,50
2,bob@test.com,Bob,IT,120,60"""


def test_parse_csv():
    result = parse_csv(CSV_CONTENT)
    assert len(result) == 2
    assert result[0]["name"] == "Alice"
    assert result[0]["payout"] == 8000


def test_parse_files(tmp_path):
    file = tmp_path / "test.csv"
    file.write_text(CSV_CONTENT)
    result = parse_files([str(file)])
    assert len(result) == 2
    assert result[1]["name"] == "Bob"
    assert result[1]["payout"] == 7200
