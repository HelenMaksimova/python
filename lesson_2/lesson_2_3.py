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
