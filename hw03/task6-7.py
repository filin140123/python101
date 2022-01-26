def int_func(text):
    return text.title()


user_text = input("Введите текст: ")

result = " ".join(list(map(int_func, user_text.split(" "))))

# # решение без int_func:
# result = user_text.title()

print(result)
