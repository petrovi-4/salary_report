import subprocess


def test_script_creates_output_file(tmp_path):
    test_csv = tmp_path / "input.csv"
    test_csv.write_text(
        "id,email,name,department,hours_worked,hourly_rate\n1,x,y,IT,100,10"
    )

    result_path = tmp_path / "result.json"

    result = subprocess.run(
        [
            "python",
            "main.py",
            str(test_csv),
            "--report",
            "payout",
            "--format",
            "json",
            "--output",
            str(result_path),
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert result_path.exists()
