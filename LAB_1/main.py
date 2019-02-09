from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square
from lab_python_oop.figure_color import FigureColor

color1 = FigureColor('синий')
color2 = FigureColor('зеленый')
color3 = FigureColor('красный')
a1 = Rectangle(3, 2, 'синий')
a2 = Circle(5, 'зеленый')
a3 = Square(5, 'красный')

print(a1)
print(a2)
print(a3)
print(a1.get_type())
print(a2.get_type())
print(a3.get_type())
