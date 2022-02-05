class Worker:
    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f"{self.name.title()} {self.surname.title()}"

    def get_total_income(self):
        return sum(self._income.values())


p = Position("kevin", "bell", "senior editor", {"wage": 700, "bonus": 100})
print(p.get_full_name())
print(p.get_total_income())
