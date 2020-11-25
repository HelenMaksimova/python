# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

class NumListError(Exception):

    def __init__(self, text='В этот список можно вносить только числа!'):
        self.txt = text


def validation(value, res_list):
    if value.isdigit():
        res_list.append(int(value))
    else:
        try:
            value = float(value)
            res_list.append(value)
        except ValueError:
            raise NumListError


result_list = []

while True:
    try:
        num = input('Введите число: ')
        if not num:
            break
        validation(num, result_list)
    except NumListError as e:
        print(e.txt, 'Попробуйте ещё раз!')

print(result_list)
