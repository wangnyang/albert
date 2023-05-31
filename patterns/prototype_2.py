# много примеров с type, prototype. все рабочие


class A:
    def __init__(self, num: int):
        self.num = num

    def method(self, arg: any):
        print(f'{self.__class__.__name__} method with arg: {arg}')

obj_1 = A(5)
NewA = type('A', (object,), {'num': 5, 'method': A.method})
obj_2 = NewA()
print(obj_1, obj_2)
print(obj_1.num, obj_2.num)
obj_1.method('hello')
obj_2.method('hello')
# выводит для 1 и 2 одно и то же:

# <__main__.A object at 0x7ff2f7a4c310> <__main__.A object at 0x7ff2f7a4c040>
# 5 5
# A method with arg: hello
# A method with arg: hello

#___________________

class Person:
    def __init__(self, name) -> None:
        self.name = name

    def say(self, text: str):
        print(f'{self.name}: {text}')

    def prototype(self):
        person_class = type(
            self.__class__.__name__,
            (object,),
            dict(self.__class__.__dict__),
        )
        return person_class(self.name)


petya = Person('Petya')
petya.say('Hello!')
new_petya = petya.prototype()
print(petya, new_petya)
new_petya.say('Hello again!')

# Petya: Hello!
# <__main__.Person object at 0x7f5425e6fdf0> <__main__.Person object at 0x7f5425e6fd90>
# Petya: Hello again!


#___________________

class Prototype:
    def prototype(self):
        person_class = type(
            self.__class__.__name__,
            self.__class__.__bases__,
            dict(self.__class__.__dict__),
        )
        return person_class(**self.__dict__)
    

class Person(Prototype):
    def __init__(self, name) -> None:
        self.name = name

    def say(self, text: str):
        print(f'{self.name}: {text}')


petya = Person('Petya')
petya.say('Hello!')
new_petya = petya.prototype()
print(petya, new_petya)
new_petya.say('Hello again!')


#___________________

class Prototype:
    def prototype(self):
        person_class = type(
            self.__class__.__name__,
            self.__class__.__bases__,
            dict(self.__class__.__dict__),
        )
        return person_class(**self.__dict__)
    

class Person(Prototype):
    def __init__(self, name, relatives: list = None) -> None:
        self.name = name
        self.relatives = relatives

    def say(self, text: str):
        print(f'{self.name}: {text}')



def show_relatives(person):
    for i, rel in enumerate(petya.relatives):
        print(f'{person.name}`s relative  #{i}: {rel.name}')

anya = Person('Anya')
vanya = Person('Vanya')
vasya = Person('Vasya')
petya = Person('Petya', relatives=[anya, vanya, vasya])
new_petya = petya.prototype()
new_petya.name = 'Petya 2.0'
show_relatives(petya)
show_relatives(new_petya)
vasya.name = 'Valera'
show_relatives(petya)
show_relatives(new_petya)


#___________________

class Prototype:
    def prototype(self):
        person_class = type(
            self.__class__.__name__,
            self.__class__.__bases__,
            dict(self.__class__.__dict__),
        )
        return person_class(**self.__dict__)
    

class Person(Prototype):
    def __init__(self, name, relatives: list = None) -> None:
        self.name = name
        self.relatives = relatives

    def say(self, text: str):
        print(f'{self.name}: {text}')



def show_relatives(person):
    for i, rel in enumerate(petya.relatives):
        print(f'{person.name}`s relative  #{i}: {rel.name}')

anya = Person('Anya')
vanya = Person('Vanya')
vasya = Person('Vasya')
petya = Person('Petya', relatives=[anya, vanya, vasya])
new_petya = petya.prototype()
new_petya.name = 'Petya 2.0'
show_relatives(petya)
show_relatives(new_petya)
vasya.name = 'Valera'
show_relatives(petya)
show_relatives(new_petya)
