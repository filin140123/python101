text = input("Введите текст: ")
splitted_text = text.split(" ")

for i, e in enumerate(splitted_text, 1):
    print(f"{i}. {e[:10]}")
