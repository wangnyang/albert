l = [1, 2, 3]
a = l      # так a и l - один и тот же объект
print(id(l), id(a))   # id одинаковые
# чтобы нормально:
a = l.copy()



from copy import deepcopy

class Person:
    def __init__(self, name: str, age: int):
        self.name, self.age = name, age

p = Person('Petya', 20)
p2 = deepcopy(p)
print(p, p2)
print(p.name, p2.name)




p = type('Person', (object,), {'name': 'Petya', 'age': 20})()

p2 = deepcopy(p)
print(p, p2)
print(p.name, p2.name)