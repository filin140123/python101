# задание 1
x, y, text = 5, 21, "test"
print(x, y, text)
user_data = input("Запрос данных у пользователя: ")
print(user_data)

# задание 2
raw_seconds = int(input("Введите время в секундах: "))
m, s = divmod(raw_seconds, 60)
h, m = divmod(m, 60)

print(f"{h:02d}:{m:02d}:{s:02d}")

# задание 3
n = input("Запрос числа n у пользователя: ")
result = int(n) + int(n+n) + int(n+n+n)
print(result)

# задание 4
'''Честно говоря, не понял, зачем здесь нужен while'''
biggest_digit = max(input("Запрос целого положительного числа: "))
print(biggest_digit)

# задание 5 и 6
revenue = float(input("Запрос выручки фирмы: "))
expenses = float(input("Запрос издержек фирмы: "))
if revenue > expenses:
    profit = revenue - expenses
    print("Прибыль — выручка больше издержек!")

    rentability = profit / revenue * 100
    print(f"Рентабельность: {rentability}%")

    workers = int(input("Запрос кол-ва сотрудников: "))
    profit_per_worker = profit / workers
    print(f"Прибыль на сотрудника: {profit_per_worker}")
else:
    print("Убыток — издержки больше выручки!")

# задание 7
a = float(input("Результат в первый день: "))
b = float(input("Цель спортсмена: "))
days = 1

while a < b:
    print(f"{days}-й день: {round(a, 2)}")
    days += 1
    a *= 1.1

print(f"{days}-й день: {round(a, 2)} — спортсмен достиг результата")
