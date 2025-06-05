# Salary report generator

### Консольная утилита на Python для генерации отчетов по заработной плате сотрудников из CSV-файлов.


#### 🚀 Быстрый старт
**_Клонируй репозиторий:_**  
```bash
  git clone https://github.com/petrovi-4/salary_report.git
  cd salary_report
```
**_Создай виртуальное окружение:_**
```bash
  python -m venv env
```
**_Активируй виртуальное окружение:_**
* Windows
```bash
  env\\Scripts\activate   
```
* macOS/Linux:
```bash
  source env/bin/activate 
```
**_Установи зависимости:_**
```bash
  pip install -r requirements.txt
```
#### 🧠 Пример использования
**_Запуск генерации отчета_**  

* Отчет в файл JSON:
```bash
  python main.py путь_к_файлам --report payout --output report.json
```
* Отчет в файл TXT:
```bash
  python main.py путь_к_файлам --report payout --output report.txt
```
* Отчет в терминал в формате JSON:
```bash
  python main.py путь_к_файлам --report payout --format json
```
* Отчет в терминал в формате TXT:
```bash
  python main.py путь_к_файлам --report payout --format text
```


**_Пример выходного JSON:_**
```JSON
{
    "Marketing": {
        "employees": [
            {
                "name": "Alice Johnson",
                "hours": 160,
                "rate": 50.0,
                "payout": 8000.0
            },
            {
                "name": "Henry Martin",
                "hours": 150,
                "rate": 35.0,
                "payout": 5250.0
            }
        ],
        "total_hours": 310,
        "total_payout": 13250.0
    },
    "Design": {
        "employees": [
            {
                "name": "Bob Smith",
                "hours": 150,
                "rate": 40.0,
                "payout": 6000.0
            },
            {
                "name": "Carol Williams",
                "hours": 170,
                "rate": 60.0,
                "payout": 10200.0
            }
        ],
        "total_hours": 320,
        "total_payout": 16200.0
    }
```

#### ✅ Запуск тестов

```bash
  pytest --cov reporting --cov-report term-missing  
```

Автор
[Мартынов Сергей](https://github.com/petrovi-4)

![GitHub User's stars](https://img.shields.io/github/stars/petrovi-4?label=Stars&style=social)
![licence](https://img.shields.io/badge/licence-GPL--3.0-green)