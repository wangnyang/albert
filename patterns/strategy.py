from typing import Tuple, List
from faker import Faker
from BTrees._OOBTree import OOBTree

class Person:
    id = 1

    def __init__(self, name: str, age: int):
        self.anem = self.age = name, age
        self.id = self.__class__.id
        self.__class__.id += 1

    def __str__(self) -> str:
        return f'{self.name}, {self.age} y.o.'


class Index:
    operators: Tuple[str]

    def search(self, attr: str, op: str, value: any):
        if op not in self.operators:
            raise NotImplementedError(f'{op} is not supported by {self.__class__.__name__} index')


class HashIndex(Index):
    operators = ('__eq__',)

    def __init__(self, data: List[any], attr: str):
        self.index = {getattr(instance, attr): instance for instance in data}

    def search(self, attr: str, op: str, value: any):
        super().search(attr, op, value)
        return self.index.get(value)

class BTreeIndex(Index):
    operators = ('__eq__', '__gt__', '__ge__', '__lt__', '__le__')

    def __init__(self, data: List[any], attr: str):
        self.index = OOBTree()
        self.index.update({getattr(instance, attr): instance for instance in data})

    def search(self, attr: str, op: str, value: any):
        super().search(attr, op, value)
        if op.startswith('__g'):
            return self.index.values(min=value, excludemin=op.endswith('t__'))
        if op.startswith('__l'):
            return self.index.values(max=value, excludemax=op.endswith('t__'))
        if op == '__eq__':
            return self.index.get(value)


class PersonManager:
    default_index_class = HashIndex

    def __init__(self, data: List[any]):
        self.data = data
        self.indexes = dict()

    def set_index(self, attr: str, index_class: Index = None):
        index_class = index_class if index_class else self.default_index_class
        self.indexes[attr] = index_class(self.data, attr)

    def seq_search(self, attr: str, op: str, value: str):
        return list(filter(lambda x: getattr(getattr(x, attr), op)(value)), self.data)

    def search(self, attr: str, op: str, value: any):
        if attr not in self.indexes:
            print(f'Index for attr {attr} not implemented')
            return self.seq_search(attr, op, value)
        try:
            return self.indexes[attr].search(attr, op, value)
        except NotImplementedError as error:
            print(error)
            print('Starting seq_search')
            return self.seq_search(attr, op, value)

faker = Faker()     
pm = PersonManager([Person(faker.name(), age) for age in range(18, 48)])
pm.set_index('id', HashIndex)
pm.set_index('age', BTreeIndex)
print(pm.search('id', '__eq__', 1))
print([str(person) for person in pm.search('age', '__le__', 20)])