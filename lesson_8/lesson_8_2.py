# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDivision(Exception):

    def __init__(self, text='Ай-ай! Нельзя делитль на ноль, никак нельзя :('):
        self.txt = text


while True:
    try:
        num_1, num_2 = [int(num) for num in input('Введите два числа через пробел: ').split()]
        if num_2 == 0:
            raise ZeroDivision
        else:
            print(f'Делим {num_1} на {num_2} и получаем {num_1 / num_2}')
            break
    except ValueError:
        print('Необходимо ввести два числа через пробел! Попробуйте ещё раз!')
        continue
    except ZeroDivision as e:
        print(f'{e.txt} Попробуйте ещё раз!')
        continue
