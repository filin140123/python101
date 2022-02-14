class WrongTypeException(Exception):
    def __init__(self):
        self.text = "Неверный тип данных. Требуется ввести число..."


mylist = []
user_input = input("Введите число. Чтобы выйти, введите пустую строку: ")
while user_input:
    try:
        if user_input.isdigit():
            mylist.append(int(user_input))
        else:
            raise WrongTypeException
    except WrongTypeException as e:
        print(e.text)

    user_input = input("Введите число. Чтобы выйти, введите пустую строку: ")

print(mylist)
