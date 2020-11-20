from abc import ABC, abstractmethod


class ClothesAbstractClass(ABC):
    @abstractmethod
    def add_clothes(self, name, parameter):
        pass

    @abstractmethod
    def clothes_tissue_consumption(self):
        pass


class Coat:

    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f'<Пальто. Размер: {str(self.size)}>'

    @property
    def tissue_consumption(self):
        return round(self.size / 6.5 + 0.5, 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 2:
            self.__size = 2
        elif size > 30:
            self.__size = 30
        else:
            self.__size = round(size)


class Suit:

    def __init__(self, height):
        self.height = height

    def __str__(self):
        return f'<Костюм. Рост: {str(self.height)}>'

    @property
    def tissue_consumption(self):
        return round(self.height * 2 + 0.3, 2)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 1:
            self.__height = 1
        elif height > 2.2:
            self.__height = 2.2
        else:
            self.__height = height


class ClothesNameError(ValueError):
    def __str__(self):
        return 'Only coat or suit can be added'


class Clothes(ClothesAbstractClass):

    CLOTHES = ['coat', 'suit']

    def __init__(self):
        self.clothes_list = []

    def __str__(self):
        return '\n'.join([f'{elem}' for elem in self.clothes_list])

    def add_clothes(self, name, parameter):
        if name not in Clothes.CLOTHES:
            raise ClothesNameError
        elif name == 'coat':
            self.clothes_list.append(Coat(parameter))
        else:
            self.clothes_list.append(Suit(parameter))

    def clothes_tissue_consumption(self):
        return sum([elem.tissue_consumption for elem in self.clothes_list])

