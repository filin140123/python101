def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Нельзя делить на ноль"
