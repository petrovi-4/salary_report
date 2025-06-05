import argparse
import json

from reporting.parser import parse_files
from reporting.reports import generate_report


def main():
    parser = argparse.ArgumentParser(description="Отчет по выплатам сотрудников.")
    parser.add_argument("files", nargs="+", help="Пути к CSV-файлам.")
    parser.add_argument("--report", choices=["payout"], required=True, help="Тип отчета")
    parser.add_argument("--format", choices=["json", "text"], default="json", help="Формат вывода")
    parser.add_argument("--output", help="Путь к выходному файлу (только формат JSON)")

    args = parser.parse_args()

    employees = parse_files(args.files)
    report_output = generate_report(employees, args.report, args.format)

    if args.format == "json":
        if not args.output:
            raise ValueError("Для формата JSON необходимо указать путь через --output")
        
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(report_output, f, ensure_ascii=False, indent=4)
        print(f"Отчет сохранен в файл {args.output}")
        
    else:
        print(report_output)


if __name__ == "__main__":
    main()