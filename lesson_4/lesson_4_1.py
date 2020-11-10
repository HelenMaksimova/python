# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def worker_salary(output: float, rate: float, prize: float) -> float:
    """
    Функция вычисляет заработную плату сотрудника исходя из выработки, почасовой ставки и премии

    :parameters:

    :output: выработка
    :rate: ставка
    :prize: премия
    """
    return output * rate + prize


script_name, arg_output, arg_rate, arg_prize = argv

result = 0

try:
    result = worker_salary(float(arg_output), float(arg_rate), float(arg_prize))
    print(f'Заработная плата работника с выработкой {float(arg_output):.2f} ч., ставкой {float(arg_rate):.2f} руб. '
          f'в час и премией {float(arg_prize):.2f} руб. составит {result:.2f} руб.')
except ValueError:
    print('Неверный тип данных!')
