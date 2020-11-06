# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

# Вариант со встроенной функцией max:
def sum_max_numbers_1(num_1, num_2, num_3):
    """Возвращает сумму двух наибольших чисел из трёх"""
    try:
        num_list = [num_1, num_2, num_3]
        max_1 = max(num_list)
        num_list.remove(max_1)
        max_2 = max(num_list)
        return max_1 + max_2
    except TypeError:
        print(f'Ошибка: неверный тип данных. Необходимо ввести числа.')


# Вариант без встроенных функций:
def sum_max_numbers_2(num_1, num_2, num_3):
    """Возвращает сумму двух наибольших чисел из трёх"""
    try:
        num_list = [num_1, num_2, num_3]
        result = 0
        for _ in range(2):
            max_num = num_list[0]
            for elem in num_list:
                max_num = elem if elem > max_num else max_num
            num_list.remove(max_num)
            result += max_num

        return result
    except TypeError:
        print(f'Ошибка: неверный тип данных. Необходимо ввести числа.')


# Вариант для любого количества чисел:
def sum_max_numbers_any(*args):
    """Возвращает сумму двух наибольших чисел из любого количества чисел"""
    try:
        num_list = list(args)
        max_1 = max(num_list)
        num_list.remove(max_1)
        max_2 = max(num_list)
        return max_1 + max_2
    except TypeError:
        print(f'Ошибка: неверный тип данных. Необходимо ввести числа.')


print(sum_max_numbers_1(1, 4, 7))
print(sum_max_numbers_2(7, 4, 1))
print(sum_max_numbers_any(1, 2, 3, 4, 7))
