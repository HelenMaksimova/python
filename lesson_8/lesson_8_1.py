# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:

    DATES = []

    def __init__(self, str_date: str):
        self.list_date = Date.extract_date(str_date)
        Date.DATES.append(self)

    def __str__(self):
        return f'{self.list_date}'

    @classmethod
    def extract_date(cls, str_date):
        try:
            list_date = [int(elem) for elem in str_date.split('-')]
            if cls.validate_date(list_date):
                return list_date
            else:
                raise ValueError
        except ValueError:
            print('Неверный формат данных! Задано минимальное возможное значение')
            return [1, 1, 1900]

    @staticmethod
    def validate_date(list_date):
        date_dict = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        day, month, year = list_date
        bool_date = False

        if month in date_dict:
            if day in range(1, date_dict[month]+1):
                if 2020 >= year >= 1900:
                    bool_date = True
                    if day == 29 and month == 2:
                        if not(year % 100 == 0 and year % 400 == 0):
                            bool_date = False

        return bool_date


with open('dates.txt') as dates_f:
    dates_list = dates_f.read().splitlines()

print('РАБОТА КЛАССА ЧЕРЕЗ СОЗДАНИЕ ОБЪЕКТОВ КЛАССА')

for date in dates_list:
    date_obj = Date(date)
    print(date_obj)

print('\nСозданные объекты класса:', *Date.DATES)

Date.DATES.clear()

print('\nРАБОТА КЛАССА ЧЕРЕЗ ВЫЗОВ @CLASSMETHOD БЕЗ СОЗДАНИЯ ОБЪЕКТОВ')

for date in dates_list:
    print(Date.extract_date(date))

print('\nСозданные объекты класса:', Date.DATES)
