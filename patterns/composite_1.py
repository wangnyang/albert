class Stationery:   # канцелярские принадлежности
    color: str
    ttl: float
    lead: str   # стержень

    def __init__(self, color, ttl) -> None:
        self.color, self.ttl = color, ttl

    def draw(self, length: float):
        print(f'{length} meters were drawn')
        new_ttl = self.ttl - length / 100
        self.ttl = new_ttl if new_ttl >= 0 else 0

    def __str__(self) -> str:
        return f'{self.color} {self.__class__.__name__} with {self.lead} lead and {self.ttl} ttl left'

class Pencil(Stationery):
    lead = 'carbon'

class Pen(Stationery):
    lead = 'ink'

class PencilCase:
    def __init__(self) -> None:
        self.__stationery = []

    def add(self, unit: Stationery):
        if isinstance(unit, Stationery):
            self.__stationery.append(unit)

    def remove(self, unit: Stationery):
        if unit in self.__stationery:
            self.__stationery.remove(unit)
        else:
            print(f'{unit} was not found in PencilCase stationery')

    def stationery(self):
        return self.__stationery


new_case = PencilCase()
new_case.add(Pen('blue', 100))
pencil = Pencil('black', 30)
new_case.add(pencil)
print([str(unit) for unit in new_case.stationery()])        # ['blue Pen with ink lead and 100 ttl left', 'black Pencil with carbon lead and 30 ttl left']
new_case.remove(pencil)
print([str(unit) for unit in new_case.stationery()])        # ['blue Pen with ink lead and 100 ttl left']