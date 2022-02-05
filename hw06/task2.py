class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self, mass_per_sq_m, cm):
        # Деление на 1000 для того, чтобы возврат значения был в тоннах, как в задании
        return (self._length * self._width * mass_per_sq_m * cm) / 1000


r = Road(20, 5000)
asphalt = r.calc_mass(25, 5)
print(asphalt)
