from lab_python_oop.Abstract_class import Figure
import math
from lab_python_oop.figure_color import FigureColor


class Circle(Figure):

    type = "Круг"

    def __init__(self, rad, color):
        self.r = rad
        self.color = FigureColor(color)

    def area(self):
        return math.pi*self.r**2

    def get_type(self):
        return self.type

    def __repr__(self):
        return 'Фигура: {}, \nРадиус: {}, \nЦвет фигуры: {}, \nПлощадь: {} \n\n'.format(self.type, self.r, self.color,
                                                                           self.area())
