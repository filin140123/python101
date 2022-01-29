# Два варианта

def my_func1(a, b, c):
    return sum(sorted([a, b, c])[1:])


def my_func2(a, b, c):
    if a < b and a < c:
        return b + c
    elif b < a and b < c:
        return a + c
    else:
        return a + b
