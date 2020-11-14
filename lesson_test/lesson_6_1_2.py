# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep
from sys import exit


class TrafficLight:
    __color = 'green'

    @staticmethod
    def running(color):
        color_dict = {'red': ('yellow', 2), 'yellow': ('green', 5), 'green': ('red', 7)}
        if not color == color_dict[TrafficLight.__color][0]:
            print('Неверный порядок переключения!')
            exit()
        print(color)
        for i in range(color_dict[TrafficLight.__color][1], 0, -1):
            print(i)
            sleep(1)
        TrafficLight.__color = color


a = TrafficLight()

while True:
    clr = input('Введите значение цвета (или нажмите Enter для выхода):')
    if not clr:
        break
    a.running(clr)
