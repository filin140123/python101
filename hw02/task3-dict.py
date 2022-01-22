seasons = {
    "winter": [1, 2, 12],
    "spring": [3, 4, 5],
    "summer": [6, 7, 8],
    "autumn": [9, 10, 11],
}

month = int(input("Введите номер месяца: "))

if month in seasons["winter"]:
    print("Зима")
elif month in seasons["spring"]:
    print("Весна")
elif month in seasons["summer"]:
    print("Лето")
elif month in seasons["autumn"]:
    print("Осень")
else:
    print("Нет такого месяца")
