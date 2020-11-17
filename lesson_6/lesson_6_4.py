# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

from random import randint


class Car:
    def __init__(self, speed=200, color='grey', name='car', is_police=False):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police

    def __repr__(self):
        return f'\nМашина:\n' \
               f'Марка: {self.name}\n' \
               f'Цвет: {self.color}\n' \
               f'Предельная скорость: {self.speed}\n' \
               f'Полицейская машина: {self.is_police}\n'

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость машины {self.name} {randint(0, self.speed)} км в ч')


class TownCar(Car):
    def show_speed(self):
        now_speed = randint(0, self.speed)
        print(f'Текущая скорость машины {self.name} {now_speed} км в ч') if now_speed <= 60 \
            else print(f'Текущая скорость машины {self.name} {now_speed} км в ч. Превышение скорости!')


class SportCar(Car):
    def __init__(self, speed=300, color='red', name='car', is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def show_speed(self):
        now_speed = randint(0, self.speed)
        print(f'Текущая скорость машины {self.name} {now_speed} км в ч') if now_speed <= 40 \
            else print(f'Текущая скорость машины {self.name} {now_speed} км в ч. Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, speed=200, color='grey', name='car', is_police=True):
        super().__init__(speed, color, name, is_police)


car = Car(160, 'blue', 'Mazda')
print(car)
car.go()
car.show_speed()
car.turn('направо')
car.stop()

town_car = TownCar(100, 'yellow', 'Audi')
print(town_car)
town_car.go()
town_car.show_speed()
town_car.turn('в сторону дома')
town_car.stop()

sport_car = SportCar(name='Ferari')
print(sport_car)
sport_car.go()
sport_car.show_speed()
sport_car.turn('к высокоскоростной автостраде')
sport_car.stop()

work_car = WorkCar(80, name='Renault')
print(work_car)
work_car.go()
work_car.show_speed()
work_car.turn('к бизнесцентру')
work_car.stop()

police_car = PoliceCar(name='BMW', color='black')
print(police_car)
police_car.go()
police_car.show_speed()
police_car.turn('вслед за машиной преступника')
police_car.stop()
