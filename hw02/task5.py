my_list = [7, 5, 3, 3, 2]

my_list.append(int(input("Введите новый элемент: ")))
my_list = sorted(my_list, reverse=True)

# # Еще вариант:
# my_list = my_list + [int(input("Введите новый элемент: "))]
# my_list = sorted(my_list, reverse=True)

print(my_list)
