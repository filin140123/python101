class Date:
    day: int
    month: int
    year: int

    def __init__(self, raw_date):
        self.raw_date = raw_date

    @classmethod
    def to_int(cls, raw_date):  # Здесь есть ощущение, что не особо верно сделал
        cls.day = int(raw_date.split('-')[0])
        cls.month = int(raw_date.split('-')[1])
        cls.year = int(raw_date.split('-')[2])

    @staticmethod
    def is_date_valid():
        day = Date.day
        month = Date.month
        year = Date.year
        # високосный год или нет?
        if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
            february = 28
        else:
            february = 29

        # вычисляем длину месяца
        if month < 1 or month > 12:
            return False
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            monthlen = 31
        elif month in [4, 6, 9, 11]:
            monthlen = 30
        else:
            monthlen = february

        # вычисляем есть ли такой день в месяце
        if 1 < day < monthlen:
            return True
        else:
            return False


d = Date("11-05-2001")
d.to_int("11-05-2001")
print(d.is_date_valid())
print(d.day)
print(d.month)
print(d.year)
