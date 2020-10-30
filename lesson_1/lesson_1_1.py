# Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
# и сохраните в переменные, выведите на экран.

var_num = 10
var_float = 10.5
var_str = 'Hello world!'
var_tuple = (1, 'abc', True)
var_list = [2, False, 45.678]
var_dict = {'a': 1, 'b': var_num, 'c': var_str}
var_set = {0, 1, 2, 3, 4}
var_bool = False

result = [var_num, var_float, var_str, var_tuple, var_list, var_dict, var_set, var_bool]

for elem in result:
    print(f'Значение переменной: {elem}', end='\n')

user_name = input('\nЭто были просто какие-то переменные.\nА теперь давай познакомимся!\nКак тебя зовут? ')
print(f'Здравствуй, {user_name}!')

user_age = int(input('Сколько тебе лет? '))
print(f'Ну надо же! Значит, тебе {user_age}')

user_work = input('А кто ты по профессии? ')
print (f'Я думаю, что {user_work} замечательная профессия!')

user_num = float(input('Введи, пожалуйста, число: '))
print(f'Пользователем по имени {user_name} было введено число {user_num}')