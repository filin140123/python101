with open("task1-file.txt", "a+", encoding="utf-8") as f:
    while True:
        user_string = input("Введите данные (пустая строка завершит программу): ")
        if user_string == "":
            break
        user_string += "\n"
        f.write(user_string)
