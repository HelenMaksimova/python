# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def exponentiation(number: float, exponent: int):
    """Принимает действительное положительное число и возводит его в отрицательную степень"""
    try:
        if number <= 0 or exponent > 0:
            raise ValueError
        return number ** int(exponent)
    except ValueError:
        print('Ошибка: переданы неверные параметры!')


def exponentiation_negative(number: float, exponent: int):
    """Принимает действительное положительное число и возводит его в отрицательную степень"""
    try:
        if number <= 0 or exponent > 0:
            raise ValueError
        if exponent == 0:
            return 1
        factor = number
        for _ in range(abs(int(exponent)) - 1):
            number *= factor
        return 1 / number
    except ValueError:
        print('Ошибка: переданы неверные параметры!')


num_base = 1
num_exp = -1
try:
    num_base = float(input('Введите положительное число: '))
    num_exp = int(input('Введите степень (отрицательное целое число): '))
except ValueError:
    print('Ошибка: неверный тип данных!')
print(f'Если {num_base} возвести в степень {num_exp} при помощи функции {exponentiation.__name__}, получится '
      f'{exponentiation(num_base, num_exp)}')
print(f'Если {num_base} возвести в степень {num_exp} при помощи функции {exponentiation_negative.__name__}, получится '
      f'{exponentiation_negative(num_base, num_exp)}')
