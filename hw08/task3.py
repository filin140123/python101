class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print('Недопустимое значение - строка и булево')
                y_or_n = input('Попробовать еще раз? y/n: ')

                if y_or_n == 'y':
                    print(t.my_input())
                elif y_or_n == 'n':
                    return 'Вы вышли'
                else:
                    return 'Вы вышли'


t = Error(1)
print(t.my_input())
