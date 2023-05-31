class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:     # именно None, тк пустой список уже подходит
            cls.__instance = super().__new__(cls)   # super() от object
        return cls.__instance


class Person(Singleton):
    def __init__(self, name) -> None:
        self.name = name


p = Person('Max')
p2 = Person('Kirill')
print(p, p2)     # одинаковые будут
print(p.name, p2.name)    # Kirill Kirill





class Singleton(type):
    __instances = dict()  #  cls: object

    def __call__(cls, *args, **kwargs):
        print('before:', cls.__instances)
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        print('after:', cls.__instances)
        return cls.__instances[cls]


class Person(metaclass=Singleton):
    def __init__(self, name) -> None:
        self.name = name

class MaxPersonBuilder(Person, metaclass=Singleton):
    def __init__(self, name: str = 'Max2288') -> None:
        super().__init__(name=name)


class KirillPersonBuilder(Person, metaclass=Singleton):
    def __init__(self, name: str = 'kirillsev1') -> None:
        super().__init__(name=name)


max2288 = MaxPersonBuilder()
kirillsev1 = KirillPersonBuilder()
