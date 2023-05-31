# OK
from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def render(text: str) -> str:
        pass

class UpperRenderer(Renderer):
    @staticmethod
    def render(text: str) -> str:
        return text.upper()
    
class TitleRenderer(Renderer):
    @staticmethod
    def render(text: str) -> str:
        return text.lower().capitalize()
    
class Page:
    def __init__(self, content: str, renderer: Renderer):
        self.content, self.renderer = content, renderer

    def set_content(self, new_content):
        if isinstance(new_content, str):
            self.__content = new_content

    def get_content(self):
        return self.renderer.render(self.__content)
    
    content = property(get_content, set_content)


main_page = Page('hello', UpperRenderer)
print(main_page.get_content())      # HELLO
