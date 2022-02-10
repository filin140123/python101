class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number - other.number > 0:
            return Cell(self.number - other.number)
        else:
            raise ValueError("Разность количества ячеек двух клеток меньше нуля")

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, row_size):
        s, e = divmod(self.number, row_size)
        result = ("*" * row_size + "\n") * s + "*" * e
        return result


# Тесты
c1 = Cell(17)
print(c1.make_order(4))
print(c1.make_order(5))

c2 = Cell(42)
print(c2.make_order(10))
print(c2.make_order(7))

c3 = c2 + c1
print(c3.make_order(8))
