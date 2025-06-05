import pytest

from reporting.reports import generate_report, format_text_report, save_report

employees = [
    {"name": "Alice", "department": "HR", "hours": 160, "rate": 50.0, "payout": 8000.0},
    {"name": "Bob", "department": "IT", "hours": 120, "rate": 60.0, "payout": 7200.0},
]


def test_generate_json_report():
    report = generate_report( "payout", employees)
    assert "HR" in report
    assert "IT" in report
    assert report["HR"]["total_payout"] == 8000.0
    assert report["IT"]["total_payout"] == 7200.0
    assert report["HR"]["total_hours"] == 160
    assert report["IT"]["total_hours"] == 120


def test_generate_text():
    report = generate_report("payout", employees)
    text_output = format_text_report(report)

    assert "HR" in text_output
    assert "IT" in text_output
    assert "Alice" in text_output
    assert "Bob" in text_output
    assert "$8000" in text_output
    assert "$7200" in text_output
    assert "160" in text_output
    assert "120" in text_output


def test_generate_report_invalid_type():
    with pytest.raises(ValueError, match="Отчет 'invalid' не поддерживается."):
        generate_report("invalid", [])


def test_save_report_invalid_format(tmp_path):
    dummy_report = {"some": "data"}
    output_path = tmp_path / "report.unknown"

    with pytest.raises(ValueError, match=r"Формат отчета 'xml' не поддерживается"):
        save_report(dummy_report, str(output_path), format="xml")
