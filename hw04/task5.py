from functools import reduce


def reducer(a, b):
    return a * b


evens = [i for i in range(100, 1001, 2)]
result = reduce(reducer, evens)
print(result)
