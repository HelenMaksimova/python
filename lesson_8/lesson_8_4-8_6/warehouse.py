class OfficeEquipment:

    def __init__(self, brand, oe_type, price=0.0,  condition=True):
        self.oe_type = oe_type
        self.brand = brand
        self.price = price
        self.condition = condition

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            self.__price = 0
        else:
            self.__price = price

    def __str__(self):
        return f'<{self.oe_type} {self.brand}>'

    def get_info(self):
        return f'Тип: {self.oe_type}\n' \
               f'Производитель: {self.brand}\n' \
               f'Цена: {self.price}\n' \
               f'Состояние: {"Исправен" if self.condition else "Неисправен"}'


class Printer(OfficeEquipment):

    def __init__(self, brand, oe_type='Принтер', price=0.0, condition=True, print_format='A4', print_type='laser'):
        super().__init__(brand, oe_type, price, condition)
        self.print_format = print_format
        self.print_type = print_type

    def get_info(self):
        res = super().get_info()
        return f'{res}\n' \
               f'Формат печати: {self.print_format}\n' \
               f'Тип печати: {self.print_type}'


class Scanner(OfficeEquipment):

    def __init__(self, brand, oe_type='Сканер', price=0.0, condition=True, scan_format='A4'):
        super().__init__(brand, oe_type, price, condition)
        self.scan_format = scan_format

    def get_info(self):
        res = super().get_info()
        return f'{res}\n' \
               f'Формат сканирования: {self.scan_format}'


class Xerox(OfficeEquipment):

    def __init__(self, brand, oe_type='Ксерокс', price=0.0, condition=True, xerox_format='A4'):
        super().__init__(brand, oe_type, price, condition)
        self.xerox_format = xerox_format

    def get_info(self):
        res = super().get_info()
        return f'{res}\n' \
               f'Формат копирования: {self.xerox_format}'


class Warehouse:

    EQUIPMENT_TYPES = {'Принтер': Printer, 'Сканер': Scanner, 'Ксерокс': Xerox}

    def __init__(self):
        self.equipment = {key: [] for key in Warehouse.EQUIPMENT_TYPES}

    def __str__(self):
        return '\n'.join([f'{key}: {len(self.equipment[key])}' for key in self.equipment])

    @classmethod
    def add_equipment_type(cls, name, cls_name):
        cls.EQUIPMENT_TYPES[name] = cls_name

    def add_equipment(self, brand, oe_type, price=0.0, condition=True, *args, **kwargs):
        if oe_type in Warehouse.EQUIPMENT_TYPES:
            oe_class = Warehouse.EQUIPMENT_TYPES.get(oe_type)
            self.equipment.get(oe_type).append(oe_class(brand, oe_type, price, condition, *args, **kwargs))
        else:
            raise WarehouseEquipmentError

    def equipment_type_count(self, oe_type):
        return len(self.equipment[oe_type])

    def equipment_type_cost(self, oe_type):
        return sum(elem.price for elem in self.equipment[oe_type])

    def equipment_count(self):
        return sum(self.equipment_type_count(key) for key in self.equipment)

    def equipment_cost(self):
        return sum(self.equipment_type_cost(key) for key in self.equipment)

    def transfer_equipment(self, department, oe_type, count=1):
        if count > self.equipment_type_count(oe_type):
            raise EquipmentCountError
        else:
            for _ in range(count):
                equip = self.equipment.get(oe_type).pop()
                department.equipment.get(oe_type).append(equip)


class Department(Warehouse):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        res = super().__str__()
        return f'{self.name}:\n{res}'


class EquipmentCountError(Exception):

    def __str__(self):
        return 'Передаваемое количество оборудования превышает имеющееся количество!'


class WarehouseEquipmentError(Exception):

    def __str__(self):
        return 'Такого типа устройства нет в списке возможных устройств!'
