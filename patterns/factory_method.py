from json import dumps

class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age

    
class PersonSerializer:
    @staticmethod
    def json(person: Person):
        return dumps(person.__dict__)
    
    @staticmethod
    def tuple(person: Person):
        return tuple(person.__dict__.items())


person = Person('Petya', 21)

# print(person)                             # <__main__.Person object at 0x7f17d6616c50>
# print(PersonSerializer.json(person))      # {"name": "Petya", "age": 21}
# print(PersonSerializer.tuple(person))     # (('name', 'Petya'), ('age', 21))




countries = ['ru', 'us']

class College:
    def __init__(self, name, location, level) -> None:
        self.name, self.location, self.level = name, location, level

class CollegeCreator:
    def create_us_college(self, name, location):
        return College(name=name, location=location, level='bachelor')

    def create_ru_college(self, name, location):
        return College(name=name, location=location, level='> Tenigin A.A')


sirius_college = CollegeCreator().create_ru_college('sirius', 'sirius')
print(sirius_college.level)

