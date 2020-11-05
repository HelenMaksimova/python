# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Решение со списком:
try:
    user_num = int(input('Введите номер месяца (целое число от 1 до 12): '))
except ValueError:
    print('Необходимо ввести число от 1 до 12!')
    user_num = 0


months_list = [
    (1, 2, 12, 'зима'),
    (3, 4, 5, 'весна'),
    (6, 7, 8, 'лето'),
    (9, 10, 11, 'осень')
]

result = 'неизвестное науке время года'

for elem in months_list:
    if user_num in elem:
        result = elem[3]
        break

print(f'Нынче на дворе {result}')

# Решение со словарём:

try:
    user_num = int(input('Введите номер месяца (целое число от 1 до 12): '))
except ValueError:
    print('Необходимо ввести число от 1 до 12!')
    user_num = 0

months_dict = {
    'зима': (1, 2, 12),
    'весна': (3, 4, 5),
    'лето': (6, 7, 8),
    'осень': (9, 10, 11)
}

result = 'неизвестное науке время года'

for key, value in months_dict.items():
    if user_num in value:
        result = key
        break

print(f'Нынче на дворе {result}')

# Другое решение со словарём:

try:
    user_num = int(input('Введите номер месяца (целое число от 1 до 12): '))
except ValueError:
    print('Необходимо ввести число от 1 до 12!')
    user_num = 0

months_dict_new = {
    1: 'зима', 2: 'зима', 3: 'весна',
    4: 'весна', 5: 'весна', 6: 'лето',
    7: 'лето', 8: 'лето', 9: 'осень',
    10: 'осень', 11: 'осень', 12: 'зима'
}

result = months_dict_new[user_num] if user_num in months_dict_new.keys() else 'неизвестное науке время года'

print(f'Нынче на дворе {result}')
