# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
from random import randint

start_list = [randint(1, 100) for _ in range(20)]

print(f'Исходный список чисел:\n{start_list}')

finish_list = [start_list[idx] for idx in range(1, len(start_list)) if start_list[idx] > start_list[idx-1]]

print(f'Список чисел, значения которых больше предыдущего элемента исходного списка:\n{finish_list}')
