from collections import defaultdict
from pprint import pprint


def generate_report(
    employees: list[dict], report_type: str, output_format: str = "json"
):
    if report_type == "payout":
        data = generate_payout_data(employees)

        if output_format == "json":
            return data
        elif output_format == "text":
            return format_payout_text(data)
        else:
            raise ValueError(f"Неизвестный формат вывода: {output_format}")
    # Тут можно без редактирования кода добавить другие отчеты
    else:
        raise ValueError(f"Неизвестный тип отчета: {report_type}")


def generate_payout_data(employees):
    departments = defaultdict(list)
    for emp in employees:
        departments[emp["department"]].append(emp)

    result = {}
    for dept, emps in departments.items():
        total_hours = sum(e["hours"] for e in emps)
        total_payout = sum(e["payout"] for e in emps)
        result[dept] = {
            "employees": [
                {
                    "name": e["name"],
                    "hours": e["hours"],
                    "rate": e["rate"],
                    "payout": e["payout"],
                }
                for e in emps
            ],
            "total_hours": total_hours,
            "total_payout": total_payout,
        }
    return result


def format_payout_text(data: dict) -> str:
    lines = []
    for department, content in data.items():
        lines.append(department)
        for emp in content["employees"]:
            lines.append(
                f"{'':<16}{emp['name']:<20}{emp['hours']:<6}{int(emp['rate']):<5}${int(emp['payout'])}"
            )
        lines.append(
            f"{'':<16}{content['total_hours']:<26}${int(content['total_payout'])}\n"
        )
    return "\n".join(lines)


# if __name__ == "__main__":
#     from parser import parse_files
#
#     file_path_1 = "../files/data1.csv"
#     file_path_2 = "../files/data2.csv"
#     file_path_3 = "../files/data3.csv"
#
#     file_paths = [file_path_1, file_path_2, file_path_3]
#
#     employees = parse_files(file_paths)
#
#     pprint(generate_report(employees, "payout"))
#     # print(generate_report(employees, "text"))
