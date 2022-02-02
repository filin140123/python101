with open("task3-file.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()
    employees = dict([s.split(" ") for s in lines])
    employees = {k: float(v) for k, v in employees.items()}

print("Сотрудники с окладом менее 20 тысяч: ")
less_than_twenty_thousand = {print(f"- {k}") for k, v in employees.items() if v < 20000}

average = round(sum(employees.values()) / len(employees), 2)
print(f"Средняя величина дохода сотрудников: {average}")
