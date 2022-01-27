# Два варианта

def my_func1(*args):
    return sum(sorted([*args])[-2:])


def my_func2(a, b, c):
    if a < b and a < c:
        return b + c
    elif b < a and b < c:
        return a + c
    else:
        return a + b
