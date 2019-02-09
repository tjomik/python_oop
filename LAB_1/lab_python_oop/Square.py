from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.figure_color import FigureColor


class Square(Rectangle):

    type = "Квадрат"

    def __init__(self, x, color):
        super().__init__(x, x, color)

    def get_type(self):
            return self.type

    def __repr__(self):
        return 'Фигура: {} ,\nСторона: {}, \nЦвет фигуры: {}, \nПлощадь: {} \n\n'.format(self.type, self.x, self.color,
                                                                            self.area())
