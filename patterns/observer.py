# анин рабочий
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass


class Observable(ABC):
    def __init__(self) -> None:
        self.subscribers = []

    def subscribe(self, subscriber: Observer):
        self.subscribers.append(subscriber)

    def notify_all(self, message: str):
        for sub in self.subscribers:
            sub.update(message)


class CollegeSiriusVKPage(Observable):
    def publish(self, post: str):
        self.notify_all(f'{self.__class__.__name__}: {post}')


class Student(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, message: str):
        print(f'{self.__class__.__name__} {self.name} got message {message}')


sir_vk_page = CollegeSiriusVKPage()
sir_vk_page.subscribe(Student('Vasya'))
sir_vk_page.subscribe(Student('Petya'))
sir_vk_page.publish('1.11.7.1 programming lessons are remote today')
