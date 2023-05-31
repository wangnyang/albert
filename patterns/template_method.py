# может это chain а не template

# Объект текста, какая-то строка
# Методы, с которыми можно работать

class Text:
    @staticmethod
    def capitalizee(text: str):
        return text.capitalize()
    
    @staticmethod
    def center(text: str, letters_num: int):
        # ***text*** длиной 20 символов
        return ('{0:*^%ss}' % (letters_num).format(text))

    @staticmethod
    def titlee(text: str):
        return text.title()

    @staticmethod
    def make_exclamatory(text: str):
        return f'{text}!'

class Content:
    def __init__(self, text: str):
        self.text = text

    def show(self):
        return Text.center(Text.make_exclamatory(Text.titlee(self.text)), 30)

college_sirius_vk = Content('запишись на стажировку или бал')
college_sirius_vk.show()
    
print(Text.center(''))
