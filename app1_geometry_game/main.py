from forms import Point, Rectangle
from person import Person

point1 = Point(2,2)
point2 = Point(6,6)

rectangle1 = Rectangle(point1, point2)

point3 = Point(4,4)
print(point3.falls_in_rectangle(rectangle1))

print(rectangle1.calculate_the_area())