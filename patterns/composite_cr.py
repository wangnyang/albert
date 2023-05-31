# Написать следующую структуру классов: 
# Есть класс продукт, каждый продукт имеет свойства: 
# name: str - имя, 
# due_date : datetime (можно и другой формат) - срок годности.  

# Используя паттерн компоновщик (Composite), написать класс Склад,
#  который имеет 	внутри скрытую коллекцию продуктов, умеет добавлять и удалять продукты внешними методами 
#  add(product: Product) -> None и remove(product: Product) -> None, 
#  а также 	имеет метод clean() -> None, который удаляет все просроченные продукты со склада.
from abc import ABC
from datetime import datetime

class Product(ABC):
    def __init__(self, name: str, due_date: datetime) -> None:
        self.name = name
        self.due_date = due_date


class Warehouse:
    def __init__(self) -> None:
        self.__products = []

    def add(self, product: Product) -> None:
        self.__products.append(product)
        print(f'{product.name} added to the Warehouse')

    def remove(self, product: Product) -> None:
        if product in self.__products:
            self.__products.remove(product)
            print(f'{product.name} removed from the Warehouse')
        else:
            print(f'product {product.name} not found in the Warehouse')

    def clean(self) -> None:
        for product in self.__products:
            if product.due_date < datetime.now():
                self.__products.remove(product)
                print(f'{product.name} removed from the Warehouse')


potato = Product('potato', datetime.now())
carrot = Product('carrot', datetime.now())
warehouse = Warehouse()
warehouse.add(potato)
warehouse.add(carrot)
warehouse.remove(carrot)
warehouse.clean()


