from math import factorial


def gen_with_yield(n):
    count = 1
    while count <= n:
        yield factorial(count)
        count += 1


for el in gen_with_yield(4):
    print(el)
