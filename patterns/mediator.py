# анин, не работает
from abc import ABC, abstractmethod
from typing import List


class Mediator(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class Worker:
    def __init__(self, name: str, mediator: Mediator, rank: int = 1) -> None:
        self.name = name
        self.mediator = mediator
        self.__rank = None
        mediator.add_sub(self)

    def send(self, message: str):
        pass

    def receive(self, message):
        print(f'{self.name} has got message: {message}')

    def get_rank(self):
        return self.__rank

    def set_rank(self, new_rank):
        if isinstance(new_rank, int) and new_rank > 0:
            if self.__rank:
                if new_rank == self.__rank:
                    print(f'{self.name} already on rank {self.__rank}')
                    return
                if new_rank > self.__rank:
                    print(f'{self.rank} was promoted')
                else:
                    print(f'{self.name} got lower rank {self.__rank}')
                self.__rank = new_rank
                return
        raise Exception('rank value must be integer and > 0')
    
    rank = property(get_rank, set_rank)

class MailChat(Mediator):
    __subs: List[Worker]

    def __init__(self):
        self.__subs = []
        self.rank = 1

    def add_sub(self, worker: Worker):
        self.__subs.append(worker)
        self.rank = worker.rank if worker.rank > self.rank else self.rank

    def remove_sub(self, worker: Worker):
        self.__subs.remove(worker)
        self.rank = max([sub.rank for sub in self.__subs])

    def update_rank(self):
        self.rank = max([sub.rank for sub in self.__subs])

    def send(self, message: str, sender: Worker):
        self.update_rank()
        if sender.rank < self.rank:
            print(f'{sender.name} who tried to send a message, has a lower rank')
            return
        for sub in self.__subs:
            sub.receive(message)


mail = MailChat()
petya, vasya, kolya = Worker('Petya', mail), Worker('Vasya', mail), Worker('Kolya', mail)
petya.rank = 3
