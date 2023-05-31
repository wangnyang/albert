# недописанный анин

class Visualizer:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def setter(self, new_value, attr):
        if isinstance(new_value, int) and new_value > 0:
            setattr(self, attr, new_value)
        else:
            print('Visualizer {attr} must be integer and greater than zero')

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, new_width: int):
        self.setter(new_width, '__width')

    @property
    def height(self):
        return self.__height
    
    @width.setter
    def heightt(self, new_height: int):
        self.setter(new_height, '__height')

    def __str__(self):
        return f'{self.__class__.__name__} with width'

class Billboard:
    def __init__(self, image_getter, viewer):
        ...
