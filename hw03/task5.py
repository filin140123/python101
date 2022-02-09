def has_special_symbol(l: list):
    for i, e in enumerate(l):
        if e == "!":
            return l[:i]
    return l


result = []

while True:
    string_of_numbers = input(
        "Введите строку чисел, разделенных пробелом ('!' завершит программу): "
    )
    splitted_string = string_of_numbers.split(" ")
    checked_list = has_special_symbol(splitted_string)

    result += list(map(int, checked_list))
    result = sum(result)

    print(f"Сумма: {result}")

    if splitted_string != checked_list:
        print("Завершение программы...")
        break

    result = [result]
