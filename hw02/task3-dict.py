seasons = {
    "Зима": [1, 2, 12],
    "Весна": [3, 4, 5],
    "Лето": [6, 7, 8],
    "Осень": [9, 10, 11],
}

month = int(input("Введите номер месяца: "))

for k, v in seasons.items():
    if month in v:
        print(k)
        break
else:
    print("Нет такого месяца")
