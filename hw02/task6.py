from pprint import pprint

stock = []
count = int(input("Сколько товаров вы хотите внести структуру данных «Товары»?: "))

for i in range(1, count + 1):
    item = input("Введите данные о товаре в формате \"название цена количество единица_измерения\": ")
    item = item.split(" ")
    item = {"название": item[0],
            "цена": item[1],
            "количество": item[2],
            "ед": item[3],
            }
    stock.append((i, item))

pprint(stock)
