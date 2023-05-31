# OK

def checker(attr: str, validator):
    def decorator(class_):          # декоратор выполняет все для checker и добавляет что-то свое...
        private_attr = f'__{attr}'
        def getter(self):
            return getattr(self, private_attr)
        def setter(self, value):
            validator(attr, value)
            setattr(self, private_attr, value)      # in Order: self.private_attr = value  if validator works
        setattr(class_, attr, property(getter, setter))         # property создает новое свойство (переменную)  
        # setattr(x, 'y', v) is equivalent to x.y = 'v'
        return class_
    return decorator       # как мы его вызываем и не передаем ему class_


def is_point(attr, point):
    if isinstance(point, tuple) and len(point) == 2:
        return isinstance(point[0], int) and isinstance(point[1], int)
    raise Exception(f'{attr} is not a point')


@checker('point_a', is_point)      # мы ставим checker в качестве декоратора для класса Order
@checker('point_b', is_point)
class Order:
    def __init__(self, point_a, point_b) -> None:
        self.point_a, self.point_b = point_a, point_b


order = Order((1,), (1, 0))   # must be ((1,0), (1, 0)) to work
