# Написать декоратор классов, который принимает название атрибута, и делает этот
# атрибут в классе скрытым и работающим через property, в котором сеттер проверяет число
# на то, что это положительный (>=0) integer.

# Написать класс Person: age: int, name: str, использовать на нём написанный декоратор
# для атрибута age.

def check_age(attr: str, validator):
    def decorator(class_):
        private_attr = f'__{attr}'
        def getter(self):
            return getattr(self, attr)
        def setter(self, new_value):
            if validator: 
                setattr(self, attr, new_value)
            else:
                raise Exception(f'age must be >= 0')
        setattr(class_, private_attr, property(getter, setter))
        return class_
    return decorator


def validate_age(age):
    if isinstance(age, int) and age >= 0:
        return True
    return False


@check_age('age', validate_age)
class Person:
    def __init__(self, age: int, name: str) -> None:
        self.age, self.name = age, name


maxeem = Person(-5, 'Maxeem')
