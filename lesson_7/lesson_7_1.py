# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.

from random import randint


class Matrix:

    def __init__(self, matrix: list):
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])

    def __str__(self):
        result = []
        for elem in self.matrix:
            result.append(f'{" ".join([str(number) for number in elem])}')

        return '\n'.join(result)

    def __add__(self, other):
        if not self.rows == other.rows or not self.columns == other.columns:
            raise ValueError('Невозможно сложить матрицы, имеющие разную разрядность')
        else:
            result = []
            for idx_row in range(self.rows):
                result.append([self.matrix[idx_row][idx_col] + other.matrix[idx_row][idx_col]
                               for idx_col in range(self.columns)])

            return Matrix(result)


while True:
    try:
        m_rows, m_columns = [int(num) for num in input('\nВведите через пробел количество строк и столбцов матрицы: ').split()]
        if m_rows <= 0 or m_columns <=0:
            raise ValueError
    except ValueError:
        print('Некорректный ввод данных! Необходимо ввести два целых положительных числа!')
        continue
    except TypeError:
        print('Некорректный ввод данных! Необходимо ввести два целых положительных числа!')
        continue

    matrix_1 = Matrix([[randint(1, 100) for _ in range(m_columns)] for _ in range(m_rows)])
    print(f'\nМатрица a:\n{matrix_1}')

    matrix_2 = Matrix([[randint(1, 100) for _ in range(m_columns)] for _ in range(m_rows)])
    print(f'\nМатрица b:\n{matrix_2}')

    print(f'\nСумма матриц a и b:\n{matrix_1 + matrix_2}')

    user_answer = input('\nДля продолжения введите "да", для выхода любой другой символ: ')
    if not user_answer == 'да':
        break
