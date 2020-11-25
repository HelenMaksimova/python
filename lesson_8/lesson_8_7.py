# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных
# экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:

    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __str__(self):

        if self.real_part == self.imaginary_part == 0:
            return '0'

        elif not self.real_part == 0 and not self.imaginary_part == 0:
            real_part = self.real_part
            imaginary_part = f' + {self.imaginary_part}'
            if self.imaginary_part < 0:
                imaginary_part = f' - {abs(self.imaginary_part)}'
            return f'{real_part}{imaginary_part}i'

        elif self.real_part == 0 and not self.imaginary_part == 0:
            return f'{self.imaginary_part}i'

        else:
            return f'{self.real_part}'

    def __add__(self, other):
        sum_real_parts = self.real_part + other.real_part
        sum_imaginary_parts = self.imaginary_part + other.imaginary_part
        return ComplexNumber(sum_real_parts, sum_imaginary_parts)

    def __mul__(self, other):
        mul_real_part = self.real_part * other.real_part - self.imaginary_part * other.imaginary_part
        mul_imaginary_part = self.real_part * other.imaginary_part + self.imaginary_part * other.real_part
        return ComplexNumber(mul_real_part, mul_imaginary_part)


while True:
    try:
        num_1_r, num_1_i = (int(elem) if float(elem).is_integer() else float(elem)
                            for elem in input('\nВведите численные значения действительной и мнимой '
                                              'частей первого числа через пробел: ').split())
        num_2_r, num_2_i = (int(elem) if float(elem).is_integer() else float(elem)
                            for elem in input('Введите численные значения действительной и мнимой '
                                              'частей второго числа через пробел: ').split())
        num_1 = ComplexNumber(num_1_r, num_1_i)
        num_2 = ComplexNumber(num_2_r, num_2_i)

        print(f'\nПри сложении комплексных чисел {num_1} и {num_2} получится {num_1 + num_2}')
        print(f'При умножении комплексного числа {num_1} на {num_2} получится {num_1 * num_2}')

        user_answer = input('\nДля выхода из программы нажмите Enter, для продолжения введите любой символ: ')

        if not user_answer:
            break

    except ValueError:
        print('\nНеобходимо ввести два числовых значения через пробел. Попробуйте ещё раз.')
