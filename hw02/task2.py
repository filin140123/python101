# Запрашиваем элементы списка у пользователя
length_of_user_list = int(input("Сколько элементов должно быть в списке?: "))
user_list = [input(f"Введите {i}-й элемент: ") for i in range(1, length_of_user_list + 1)]

# Если количество элементов в списке нечетное, вычитаем единицу из его длины
if length_of_user_list % 2 != 0:
    length_of_user_list -= 1

# Изначальные индексы
pos1, pos2 = 0, 1

# Цикл для обмена элементов
for i in range(int(length_of_user_list / 2)):
    user_list[pos1], user_list[pos2] = user_list[pos2], user_list[pos1]
    pos1 += 2
    pos2 += 2


print(user_list)
