# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_num = input('Введите число: ')

result = int(user_num) + int(user_num*2) + int(user_num*3)

print(f'Сумма чисел {user_num}, {user_num*2} и {user_num*3} равна {result}')
