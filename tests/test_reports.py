from reporting.reports import generate_report

employees = [
    {"name": "Alice", "department": "HR", "hours": 160, "rate": 50.0, "payout": 8000.0},
    {"name": "Bob", "department": "IT", "hours": 120, "rate": 60.0, "payout": 7200.0},
]


def test_generate_json_report():
    report = generate_report(employees, "payout", "json")
    assert "HR" in report
    assert report["HR"]["total_payout"] == 8000.0


def test_generate_text():
    report = generate_report(employees, "payout", "text")
    assert "Alice" in report
    assert "Bob" in report
    assert "$8000" in report
