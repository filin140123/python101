class CustomZeroDivision:
    def __init__(self, div, den):
        self.div = float(div)
        self.den = float(den)

    def division(self):
        try:
            return self.div / self.den
        except:
            return "Деление на ноль!"


d1 = CustomZeroDivision(input("Делимое: "), input("Делитель: "))
print(d1.division())
d2 = CustomZeroDivision(input("Делимое: "), input("Делитель: "))
print(d2.division())
d3 = CustomZeroDivision(input("Делимое: "), input("Делитель: "))
print(d3.division())
