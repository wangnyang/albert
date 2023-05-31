# анин с ошибкой в самом низу, и принты не дописаны
from random import choice
from string import ascii_lowercase

class RandomLetter:
    def __init__(self, letter_num: int) -> None:
        self.num = letter_num
        self.current = 0
        self.used = []

    def __next__(self):
        if self.current < self.num:
            letter = choice(ascii_lowercase)
            while letter in self.used:
                letter = choice(ascii_lowercase)
            self.current += 1
            return letter
        else:
            raise StopIteration

    def __iter__(self):
        return self


letter_iterator = RandomLetter(2)
for letter in letter_iterator:
    print(letter)


class Iterator:
    def __init__(self):
        self._instances = []

    def add(self, instance: any):
        self._instances.append(instance)

    def remove(self, instance):
        self._instances.remove(instance)

    def __next__(self):
        if self._instances:
            return self._instances.pop()
        else:
            raise StopIteration


class Person:
    iterator = Iterator()

    def __init__(self, name: str, age: int):
        self.name, self.age = name, age
        Person.iterator.add(self)

    def __del__(self):
        Person.iterator.remove(self)

    def __str__(self):
        return f'{self.__class__.__name__} {self.name}, {self.age} y.o.'


petya = Person('Petya', 20)
vasya = Person('Vasya', 19)
vlad = Person('Vlad', 18)
for person in Person.iterator:
    print(person)
