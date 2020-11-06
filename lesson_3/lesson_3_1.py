# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division_numbers(num_1, num_2):
    """Возвращает результат деления двух чисел"""
    try:
        return float(num_1) / float(num_2)
    except ZeroDivisionError:
        print(f'Ошибка: деление на ноль!')
    except ValueError:
        print(f'Ошибка: неверный тип данных!')


number_1 = input('Введите делимое: ')
number_2 = input('Введите делитель: ')

print(division_numbers(number_1, number_2))
