def count_to_ten(x: int):
    count = x
    while count <= 10:
        yield count
        count += 1


c = count_to_ten(3)
for n in c:
    print(n)
