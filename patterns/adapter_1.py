# не дописала

from abc import ABC
from random import randrange

class Transformer(ABC):
    voltage: int
    fluctuations_range: float

    def get_power(self):
        return f'напряжение {self.voltage}'

    def get_current_power(self):
        voltage = self.voltage + randrange(-self.fluctuations_range, self.fluctuations_range)
        return f'напряжение {self.voltage}'


class Tranformer220(Transformer):
    voltage = 220
    fluctuations_range = 10.0


class Tranformer380(Transformer):
    voltage = 380
    fluctuations_range = 15.0


class PowerSocket:
    def __init__(self, transformer: Transformer):
        self.transformer = transformer

    def set_transformer(self, transformer: Transformer):
        if not isinstance(transformer, Transformer):
            raise Exception(f'{self.__class__.__name__} tranformer must be ...')
