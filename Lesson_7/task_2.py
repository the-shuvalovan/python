from abc import ABC, abstractmethod
import math


class Clothes(ABC):
    @abstractmethod
    def spent(self, param):
        pass


class Coat(Clothes):
    def spent(self, param):
        spent = math.ceil(param / 6.5 + 0.5)
        print(f'Расход ткани: {spent}')
        return spent


class Suit(Clothes):
    def spent(self, param):
        self.param = param
        spent = math.ceil((param * 2 + 0.3) / 100)
        print(f'Расход ткани: {spent}')
        return spent


a = Coat()
a.spent(50)

b = Suit()
b.spent(180)
