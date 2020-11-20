# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
# и целочисленное (с округлением до целого) деление клеток, соответственно.

class CellOperationError(ValueError):
    def __str__(self):
        return 'Опрецию выполнить невозможно!'


class Cell:

    cells_id = 0

    def __init__(self, cell_size):
        if cell_size <= 0 or not float(cell_size).is_integer():
            raise ValueError('Количество ячеек в клетке должно быть целым числом больше нуля')
        else:
            self.cell_size = cell_size
            Cell.cells_id += 1
            self.cell_id = f'{Cell.cells_id:03}'
            self.order = None

    def __str__(self):
        return f'<Клетка. Ячеек: {str(self.cell_size)}. ID: {self.cell_id}>'

    def __add__(self, other):
        result = self.cell_size + other.cell_size
        return Cell(result)

    def __sub__(self, other):
        result = self.cell_size - other.cell_size
        if result > 0:
            return Cell(result)
        else:
            raise CellOperationError

    def __mul__(self, other):
        result = self.cell_size * other.cell_size
        return Cell(result)

    def __truediv__(self, other):
        result = self.cell_size // other.cell_size
        if result > 0:
            return Cell(result)
        else:
            raise CellOperationError

    def make_order(self, nucleus):
        result = [('*' * self.cell_size)[i:i+nucleus] for i in range(0, self.cell_size, nucleus)]
        self.order = '\n'.join(result)
