# trees

# Leaf: width, height, color
# width: 1-3
# length: 1-10
# color: 'FF0000', '00FF00' or '0000FF'
from random import randint, choice
from psutil import Process

class FlyWeight:
    pass

class Leaf:
    instances = {}

    def __new__(cls, width: int, length: int, color: str):
        key = f'{width}_{length}_{color}'
        if key in cls.instances:
            return cls.instances[key]
        instance = type(cls.__name__, (object), {'width': width, 'length': length, 'color': color})
        cls.instances[key] = instance
        return instance

    def __init__(self, width: int, length: int, color: str) -> None:
        self.width, self.length, self.color = width, length, color


colors = ('FF0000', '00FF00', '0000FF')
leafs = [Leaf(randint(1, 3), randint(1, 10), choice(colors)) for _ in range(10 ** 6)]
print(f'Memory usage: {Process().memory_info().vms / 1024 / 1024} Мегабайт')
