# Решение с **
def power1(x: float, y: int):
    return x ** y


# Решение без **
def power2(x: float, y: int):
    p = 1
    for i in range(1, -y + 1):
        p /= x
    return p
