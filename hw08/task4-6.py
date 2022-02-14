class StoreMashines:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.num = number_of_lists
        self.store_full = []
        self.store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            u = input(f'Введите наименование ')
            p = int(input(f'Введите цену за ед '))
            q = int(input(f'Введите количество '))
            unique = {'Модель устройства': u, 'Цена за ед': p, 'Количество': q}
            self.my_unit.update(unique)
            self.store.append(self.my_unit)
            print(f'Текущий список -\n {self.store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - q, продолжение - Enter')
        q = input('---> ')
        if q == 'q':
            self.store_full.append(self.store)
            print(f'Весь склад -\n {self.store_full}')
            return 'Выход'
        else:
            return StoreMashines.reception(self)


class Printer(StoreMashines):
    def to_print(self):
        return f'Печатаем {self.num} раз'


class Scanner(StoreMashines):
    def to_scan(self):
        return f'Сканируем {self.num} раз'


class Copier(StoreMashines):
    def to_copier(self):
        return f'Копируем {self.num} раз'


unit_1 = Printer('HP', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('ASUS', 1500, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())
