# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw():
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title='Ручка'):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} рисует тонкую линию')


class Pencil(Stationery):
    def __init__(self, title='Карандаш'):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} рисует кружочки средней толщины')


class Handle(Stationery):
    def __init__(self, title='Маркер'):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} рисует толстую волнистую линию')


some_stationery = Stationery('Какая-то канцелярская принадлежность')
some_stationery.draw()

some_pen = Pen()
some_pen.draw()

some_pencil = Pencil()
some_pencil.draw()

some_handle = Handle()
some_handle.draw()
