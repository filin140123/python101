class Cloth:
    def __init__(self, name, V, H):
        self.name = name
        self.V = V
        self.H = H

    @property
    def coat(self):
        return self.V / 6.5 + 0.5

    @property
    def suit(self):
        return 2 * self.H + 0.3


c1 = Cloth("пальто", 52, 6.8)
print(c1.coat)
c2 = Cloth("костюм", 48, 6.5)
print(c2.suit)
