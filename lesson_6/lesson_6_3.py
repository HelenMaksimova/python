# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
# с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name, self.surname, self.position = name, surname, position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


workers = []

while True:
    w_name, w_surname, w_position = input('\nВведите имя, фамилию и должность сотрудника через пробел: ').split()
    w_wage, w_bonus = map(float, input('Введите оклад и премию сотрудника через пробел: ').split())
    workers.append(Position(w_name, w_surname, w_position, w_wage, w_bonus))
    exit_ans = input('\nПродолжить? (да / любой символ)').lower()
    if not exit_ans == 'да':
        break

for elem in workers:
    print(f'\n{elem.get_full_name()}: доход {elem.get_total_income()}')
    print(f'Детально: имя: {elem.name}, фамилия: {elem.surname}, должность: {elem.position}')
