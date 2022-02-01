from sys import argv


def salary(hours, rph, bonus):
    result = float(hours) * float(rph) + float(bonus)
    if result % 10 == 0:
        result = int(result)
    return result


script_name, h, r, b = argv
print(salary(h, r, b))
