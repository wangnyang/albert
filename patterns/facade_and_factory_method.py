# Фасад, фабричный метод
# Car
#  method build_supercar (engine, tires, body, transmission) - fabric method
# tires - шины, transmission - коробка передач, body - машина сама
# tires have radius, pressure, normal_pressure
# body has height, length, width, colour
# engine has hp (мощность), manf (производитель)
# transmission has current, num (количество передач)

# facade:
# method check_tires
# method get_size (габаритные размеры автомобиля)
from typing import List

class Tyre:
    def __init__(self, pressure: float, normal_pressure: float, radius: int =14) -> None:
        self.radius = radius
        self.pressure = pressure
        self.normal_pressure = normal_pressure

class Body:
    def __init__(self, height: int, length: int, width: int, colour: str) -> None:
        self.height = height
        self.length = length
        self.width = width
        self.colour = colour

class Engine:
    def __init__(self, hp: int, manf: str) -> None:
        self.hp = hp
        self.manf = manf

class Transmission:
    standart_peredachi = ['N', 'P', 'R']

    def __init__(self, peredachi: int) -> None:
        self.standart_peredachi.extend([f'D{i}' for i in range(peredachi)])
        self.current = self.standart_peredachi[1]


class Car:
    def __init__(self, engine: Engine, tires: List[Tyre], body: Body, transmission: Transmission) -> None:
        self.engine = engine
        self.tires = tires
        self.body = body
        self.transmission = transmission

    # фабричный метод
    @classmethod
    def build_supercar(cls):
        jz2 = Engine(800, 'Toyota')
        s_body = Body(1500, 3500, 1999, 'Blue')
        tires = [Tyre(1.9, 2.2, 17) for _ in range(4)]
        transmission = Transmission(6)
        return cls(jz2, tires, s_body, transmission)

    # фасады:
    def check_tires(self) -> bool:
        for tyre in self.tires:
            low_threshold = tyre.normal_pressure * 0.95
            high_threshold = tyre.normal_pressure * 1.05
            if tyre.pressure < low_threshold or tyre.pressure > high_threshold:
                return False
        return True

    def get_size(self):
        max_radius = [max(tyre.radius) for tyre in self.tires]
        return max_radius + self.body.height
