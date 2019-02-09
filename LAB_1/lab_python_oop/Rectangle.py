from lab_python_oop.Abstract_class import Figure
from lab_python_oop.figure_color import FigureColor

class Rectangle(Figure):

    type = "Прямоугольник"

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = FigureColor(color)

    def area(self):
        return self.x * self.y

    def get_type(self):
        return self.type

    def __repr__(self):
        return 'Фигура: {}, \nДлина: {}, \nВысота: {}, \nЦвет фигуры: {}, \nПлощадь: {}\n\n'.format(self.type,
                                                                                self.x, self.y, self.color, self.area())
