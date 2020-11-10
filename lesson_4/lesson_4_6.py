# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count
from itertools import cycle

FINISH = 'q'

print('\nДля вывода следующего значения итератора нажмите Enter, для выхода из итератора введите "q"\n')

# задание а)

start_number = int(input('Введите начальное целое число:'))

exit_str = ''

for number in count(start_number):
    if exit_str == FINISH:
        break
    print(number, end='')
    exit_str = input()


# задание b)

start_list = input('\nВведите элементы, разделённые пробелами: ').split()

exit_str = ''

for elem in cycle(start_list):
    if exit_str == FINISH:
        break
    print(elem, end='')
    exit_str = input()

