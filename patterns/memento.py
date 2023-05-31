# полный рабочий код

# Хранитель
# Что делать с Василием? Он на глазах стареет

class Memento:
    def save(self):
        self._saved_point = {attr: self.__dict__[attr] for attr in self.__dict__}
        #сохранить текущее состояние 

    def restore(self):
        for attr in self._saved_point:
            setattr(self, attr, self._saved_point[attr])

class Person(Memento):
    def __init__(self, name: str, age: int):
        self.name, self.age = name, age

    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.name}, {self.age} y. o.'

vasya = Person('Vasylyi', 36)
vasya.save()
print(vasya)
vasya.age = 37
print(vasya)
vasya.restore()
print(vasya)
