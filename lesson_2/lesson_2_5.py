# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться после них.

user_list = [5, 2, 2, 1]

print(f'Изначально рейтинг выглядит так: {user_list}')

confirm = True

while confirm:
    try:
        user_answer = int(input('Введите новую позицию рейтинга: '))
    except ValueError:
        print(f'Ошибка:! Необходимо ввести целое число!')
        continue

    new_pos = 0

    for elem in user_list:
        if elem >= user_answer:
            new_pos = user_list.index(elem) + user_list.count(elem)

    user_list.insert(new_pos, user_answer)

    user_confirm = input('Ввести следующий элемент рейтинга? (да / любой символ)')
    confirm = True if user_confirm == 'да' else False

print(f'Теперь рейтинг выглядит так: {user_list}')
