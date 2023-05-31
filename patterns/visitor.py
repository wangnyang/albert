# полный рабочий код

# Посетитель определяет, что ему делать
# У посетителя метод ходить в ресторан, ресторан принимает этот метод

from typing import List
from random import choice

class Building:
    def __init__(self, items):
        self.items = items

class Restaurant(Building):
    pass

class Gallery(Building):
    pass

class College(Building):
    pass

class Hospital(Building):
    def __init__(self, items) -> None:
        pass

class Visitor:
    def __init__(self, name: str, age: int) -> None:
        self.name, self.age = name, age 

    def visit(self, building: Building):
        if isinstance(building, Restaurant):
            dish = choice(building.items)
            print(f'Enjoying a meal called {dish} in a restauraunt')
        elif isinstance(building, Gallery):
            pieces = list(filter(lambda x: not x.startswith('modern'), building.items))
            print(f'Contemplating the pieces of art: {pieces}')
        else:
            print('Unknown type of building. Skipping..')

medusa = Restaurant(['expensive sushi', 'bad sushi'])
erarta = Gallery(['modern art', 'nichegoneponyal art'])
sirius = College(['Developing programming modules', 'Databases']) 
kb57 = Hospital(['X Ray', 'Ray Charles', 'Manta Ray', 'Rey Palpatine'])

vasya = Visitor('Vasya', 10)
vasya.visit(medusa)
vasya.visit(erarta)
vasya.visit(sirius)
vasya.visit(kb57)
