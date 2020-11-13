# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint

with open('numbers.txt', 'w+', encoding='UTF-8') as numbers_f:
    number_list = (randint(1, 1000) for _ in range(10))
    print(*number_list, file=numbers_f)
    numbers_f.seek(0)
    numbers_sum = sum(int(elem) for elem in numbers_f.readline().rstrip('\n').split())

print(f'Сумма чисел в файле "{numbers_f.name}" равна {numbers_sum}')

