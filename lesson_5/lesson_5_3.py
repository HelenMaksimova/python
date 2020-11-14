# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

LIMIT_SALARY = 20000.0

with open('workers.txt', encoding='UTF-8') as workers_f:
    workers_list = [elem.rstrip('\n').split() for elem in workers_f.readlines()]

low_salary = (elem[0] for elem in workers_list if float(elem[1]) < LIMIT_SALARY)

workers_profit = sum((float(elem[1])) for elem in workers_list)/len(workers_list)

print(f'Всего сотрудников: {len(workers_list)}. Средняя величина дохода сотрудников: {workers_profit:.2f}.\n'
      f'Сотрудники, получающие меньше {LIMIT_SALARY:.2f} руб.:')
print(*low_salary, sep='\n')
