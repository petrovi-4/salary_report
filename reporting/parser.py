RATE_FIELDS = {"hourly_rate", "rate", "salary"}


def parse_csv(content: str) -> list[dict[str, str | float | int]]:
    """
    Преобразует CSV-строку в список словарей с данными о сотрудниках.

    Каждая строка CSV интерпретируется как запись о сотруднике.
    Поддерживаются поля с разными названиями для ставки (hourly_rate, rate, salary).
    Вычисляется выплата (payout) как произведение часов и ставки.

    Параметры:
    content (str): Содержимое CSV-файла в виде строки.

    Возвращает:
    list[dict[str, str | float | int]]: Список сотрудников с полями name, department, hours, rate, payout.
    """
    lines = content.strip().split("\n")
    normalized = []

    if not lines:
        return normalized

    # Заголовки.
    raw_header = lines[0].split(",")
    header = [h.strip() for h in raw_header]

    # Данные.
    rows = lines[1:]
    for line in rows:
        raw_values = line.split(",")
        values = [v.strip() for v in raw_values]

        data = dict(zip(header, values))

        # Находим ставку
        rate = None
        for key in RATE_FIELDS:
            if key in data:
                rate = float(data[key])
                break

        if rate is None:
            continue  # Если ставка не найдена, пропускаем строку.

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
    Читает и объединяет данные сотрудников из нескольких CSV-файлов.

    Каждый файл обрабатывается функцией parse_csv.
    Ошибки доступа к файлу обрабатываются и выводятся в консоль.

    Параметры:
    file_path (list[str]): Пути к CSV-файлам.

    Возвращает:
    list[dict[str, str | float | int]]: Список всех сотрудников из всех файлов.
    """
    employees = []
    for path in file_path:
        try:
            with open(path, encoding="utf-8") as f:
                content = f.read()
                parsed = parse_csv(content)
                for emp in parsed:
                    employees.append(emp)
        except FileNotFoundError:
            print(f"Файл не найден: {path}")
        except PermissionError:
            print(f"Нет доступа к файлу {path}")
    return employees
