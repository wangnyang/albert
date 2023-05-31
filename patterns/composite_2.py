# компоновщик OK
# есть окно, в нем виджеты, они не должны заслонять друг друга и выходить за границы окна

class Widget:
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class Window:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.widgets = []

    def not_collides(self, widget):
        for target in self.widgets:
            if target is widget:
                continue
            is_lower = widget.y + widget.height < target.y
            is_higher = target.y + target.height < widget.y
            is_right = target.x + target.width < widget.x
            is_left = widget.x + widget.width < target.x
            if widget.x < widget.x:     # on the left
                if not (is_left or is_lower or is_higher):
                    return False
            if widget.x >= target.x:
                if not (is_right or is_lower or is_higher):
                    return False
            if widget.y < target.y:
                if not (is_lower or is_right or is_left):
                    return False
            if widget.y >= target.y:
                if not (is_higher or is_right or is_left):
                    return False
        return True


    def add(self, widget):
        if self.not_collides(widget):
            self.widgets.append(widget)
            print('OK')
        else:
            print('You are wrong!')


widget_1 = Widget(1, 1, 2, 2)
widget_2 = Widget(3, 3, 2, 2)
window = Window(10, 10)
window.add(widget_1)
window.add(widget_2)
