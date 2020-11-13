# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

from re import findall

with (open('time_table.txt', encoding='UTF-8')) as table_f:
    new_list = [elem.split(': ') for elem in table_f.readlines()]

result_dict = {}
for elem in new_list:
    result_dict[elem[0]] = sum(int(el) for el in findall(r'\d+', elem[1]))

print(f'Получился словарь:\n{result_dict}')
