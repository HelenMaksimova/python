# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce

start_list = [elem for elem in range(100, 1001) if elem % 2 == 0]

print(f'Список чётных чисел от 100 до 1000:\n{start_list}')

product_list = reduce(lambda num_1, num_2: num_1 * num_2, start_list)

print(f'Произведение всех чисел в списке равно: {product_list}')
