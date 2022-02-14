class CustomZeroDivision(Exception):
    def __init__(self):
        self.text = "Деление на ноль :)"


def division(div, den):
    try:
        if den == 0:
            raise CustomZeroDivision
        print(div / den)
    except CustomZeroDivision as e:
        print(e.text)


a, b = int(input("Делимое: ")), int(input("Делитель: "))
division(a, b)
