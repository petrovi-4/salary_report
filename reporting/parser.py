from pprint import pprint

RATE_FIELDS = {"hourly_rate", "rate", "salary"}


def parse_csv(content: str) -> list[dict[str, str | float | int]]:
    """
    Разбирает CSV-содержимое в виде строки и возвращает список сотрудников.

    Каждая строка CSV конвертируется в словарь с полями:
    - name: имя сотрудника (str)
    - department: отдел (str)
    - hours: количество отработанных часов (int)
    - rate: ставка оплаты (float)
    - payout: итоговая выплата (float)

    Параметры:
    content (str): Содержимое CSV-файла в виде строки.

    Возвращает:
    list[dict[str, str | float | int]]: Список словарей с информацией о сотрудниках.
    """
    lines = content.strip().splitlines()
    if not lines:
        return []

    # Заголовки
    raw_header = lines[0].split(",")
    header = []
    for h in raw_header:
        header.append(h.strip())

    # Данные
    rows = lines[1:]
    normalized = []
    for line in rows:
        raw_values = line.split(",")
        values = []
        for v in raw_values:
            values.append(v.strip())

        data = dict(zip(header, values))

        # Находим ставку
        rate = None
        for key in RATE_FIELDS:
            if key in data:
                rate = float(data[key])
                break

        if rate is None:
            continue  # Если ставка не найдена, пропускаем строку

        hours = int(data["hours_worked"])
        payout = hours * rate

        employee = {
            "name": data["name"],
            "department": data["department"],
            "hours": hours,
            "rate": rate,
            "payout": payout,
        }
        normalized.append(employee)

    return normalized


def parse_files(file_path: list[str]) -> list[dict[str, str]]:
    """
    Обрабатывает список путей к CSV-файлам и объединяет данные из всех файлов.

    Каждый файл читается, парсится с помощью parse_csv,
    и данные сотрудников добавляются в общий список.

    Параметры:
    file_path (list[str]): Список строк — путей к CSV-файлам.

    Возвращает:
    list[dict[str, str | float | int]]: Объединённый список всех сотрудников.
    """
    employees = []
    for path in file_path:
        with open(path, encoding="utf-8") as f:
            content = f.read()
            employees.extend(parse_csv(content))
    return employees


if __name__ == "__main__":
    file_path_1 = "../files/data1.csv"
    file_path_2 = "../files/data2.csv"
    file_path_3 = "../files/data3.csv"

    file_paths = [file_path_1, file_path_2, file_path_3]

    pprint(parse_files(file_paths))
