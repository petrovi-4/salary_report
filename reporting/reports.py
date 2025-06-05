import json
from collections import defaultdict
from typing import Any


def generate_report(report_type: str, employees: list[dict[str, str | float | int]]) -> dict[str, Any]:
    """
    Генерирует отчет по заданному типу на основе списка сотрудников.

    Поддерживаемые типы отчетов:
    - "payout": отчет по выплатам по отделам.

    Параметры:
    report_type (str): Тип отчета (например, 'payout').
    employees (list): Список словарей с данными сотрудников.

    Возвращает:
    dict[str, Any]: Структурированный отчет.

    Исключения:
    ValueError: Если передан неподдерживаемый тип отчета.
    """
    if report_type == "payout":
        return generate_payout_report(employees)
    else:
        raise ValueError(f"Отчет '{report_type}' не поддерживается.")


def generate_payout_report(employees: list[dict[str, str | float | int]]) -> dict[str, Any]:
    """
    Генерирует отчет по выплатам для каждого отдела.

    Параметры:
    employees (list): Список словарей с данными сотрудников.

    Возвращает:
    dict[str, Any]: Отчет, сгруппированный по отделам, с общей суммой часов и выплат.
    """
    departments = defaultdict(list)
    report_data = {}

    for emp in employees:
        department = emp["department"]
        departments[department].append(emp)

    for department in departments:
        total_hours = 0
        total_payout = 0
        emps = departments[department]
        report_data[department] = {
            "employees": [],
            "total_hours": 0,
            "total_payout": 0
        }

        for emp in emps:
            report_data[department]["employees"].append(emp)
            total_hours += emp["hours"]
            total_payout += emp["payout"]

        report_data[department]["total_hours"] = total_hours
        report_data[department]["total_payout"] = total_payout

    return report_data


def format_text_report(report: dict[str, Any]) -> str:
    """
    Форматирует отчет в виде текстовой таблицы.

    Параметры:
    report (dict): Сгенерированный отчет по отделам.

    Возвращает:
    str: Текстовое представление отчета.
    """
    lines = []
    header = f"{'':<16}{'name':<20}{'hours':<6}{'rate':<6}{'payout'}"
    lines.append(header)

    for department, data in report.items():
        lines.append(department)
        for emp in data["employees"]:
            name = emp["name"]
            hours = emp["hours"]
            rate = int(emp["rate"])
            payout = int(emp["payout"])
            lines.append(f"{'':<16}{name:<20}{hours:<6}{rate:<6}${payout}")
        total_hours = data["total_hours"]
        total_payout = data["total_payout"]
        lines.append(f"{'':<16}{total_hours:<26}${total_payout}")
        lines.append("")

    return "\n".join(lines)


def save_report(report: dict[str, Any], output_path: str, format: str = "json") -> None:
    """
    Сохраняет отчет в указанный файл в выбранном формате.

    Поддерживаемые форматы:
    - 'json': сохраняет как JSON-файл
    - 'text': сохраняет как текстовую таблицу

    Параметры:
    report (dict): Сгенерированный отчет.
    output_path (str): Путь к файлу для сохранения.
    format (str): Формат сохранения ('json' или 'text').

    Исключения:
    ValueError: Если передан неподдерживаемый формат.
    """
    if format == "json":
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=4)
    elif format == "text":
        text = format_text_report(report)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
    else:
        raise ValueError(f"Формат отчета '{format}' не поддерживается")
