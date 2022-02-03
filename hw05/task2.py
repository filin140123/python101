with open("task2-file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    line_count = len(lines)
    print(f"Кол-во строк в файле: {line_count}")
    for i, s in enumerate(lines, 1):
        word_count = len(s.split(" "))
        print(f"Кол-во слов в {i}-й строке: {word_count}")
