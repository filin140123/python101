class Date:
    def __init__(self, raw_date):
        self.raw_date = raw_date

    @classmethod
    def to_int(cls, raw_date):
        try:
            day, month, year = raw_date.split('-')
            return int(day), int(month), int(year)
        except ValueError as e:
            print(f"Не удалось выделить дату: {e}")

    @staticmethod
    def is_date_valid(date_to_check):
        try:
            day, month, year = date_to_check
        except TypeError as e:
            return f"Не удалось считать дату: {e}"
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
print(d.raw_date)  # 11-05-2001
print(d.is_date_valid(d.to_int("11-05-2001")))  # True
print(d.to_int("11-05-2001"))  # (11, 5, 2001)
print(d.is_date_valid(d.to_int("31-02-2011")))  # False, т.к. 31 февраля не существует
print(d.is_date_valid(d.to_int("01011999")))  # ValueError, TypeError
