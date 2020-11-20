# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.

from random import randint


class Road:

    def __init__(self, length=1, width=1):
        self._length, self._width = length, width

    def __repr__(self):
        return f'Дорога.\nШирина полотна: {self._width} м\nДлина полотна: {self._length} м'

    def asphalt_mass(self, mass=25, thickness=5):
        return (self._width * self._length * mass * thickness) / 1000


r_length, r_width, r_mass, r_thickness = randint(1000, 10000), randint(20, 50), randint(20, 50), randint(1, 10)

road = Road(r_length, r_width)
print(road)
print(f'Для покрытия всего дорожного полотна потребуется асфальта: {road.asphalt_mass(r_mass, r_thickness)} т'
      f' (при массе асфальта {r_mass} кг на 1 м и толщине {r_thickness} см)')
