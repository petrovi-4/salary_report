import argparse
import json

from reporting.parser import parse_files
from reporting.reports import generate_report, save_report, format_text_report


def main():
    """
    Основная функция командной строки для генерации отчета по зарплатам.

    Обрабатывает аргументы командной строки:
    - файлы с данными;
    - тип отчета (например, payout);
    - формат вывода (json или text);
    - путь к выходному файлу (необязателен).

    В зависимости от параметров либо выводит отчет в консоль,
    либо сохраняет его в указанный файл.
    """
    parser = argparse.ArgumentParser(description="Отчет по выплатам сотрудников.")
    parser.add_argument("files", nargs="+", help="Пути к CSV-файлам.")
    parser.add_argument("--report", required=True, help="Тип отчета (например, payout")
    parser.add_argument("--format", choices=["json", "text"], default="json", help="Формат вывода")
    parser.add_argument("--output", help="Имя выходного файла")

    args = parser.parse_args()
    employees = parse_files(args.files)

    if not employees:
        print("Нет данных для формирования отчета.")
        return

    try:
        report = generate_report(args.report, employees)
    except ValueError as e:
        print(f"Ошибка: {e}")
        return

    if args.output:
        save_report(report, args.output, args.format)
        print(f"Отчет сохранен в {args.output}")
    else:
        if args.format == "json":
            print(json.dumps(report, ensure_ascii=False, indent=4))
        elif args.format == "text":
            print(format_text_report(report))


if __name__ == "__main__":
    main()
