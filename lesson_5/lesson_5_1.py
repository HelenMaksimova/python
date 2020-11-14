# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('test.txt', 'w', encoding='UTF-8') as test_f:
    while True:
        user_str = input()
        if not user_str:
            break
        print(user_str, file=test_f)
