with open("task5-file.txt", "w", encoding="utf-8") as f:
    f.write("14 22 31 48 56 65 75 84 99")

with open("task5-file.txt", "r", encoding="utf-8") as r:
    numbers = sum([int(i) for i in r.read().split(" ")])
    print(numbers)
