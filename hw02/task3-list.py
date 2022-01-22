winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

month = int(input("Введите номер месяца: "))

if month in winter:
    print("Зима")
elif month in spring:
    print("Весна")
elif month in summer:
    print("Лето")
elif month in autumn:
    print("Осень")
else:
    print("Нет такого месяца")
