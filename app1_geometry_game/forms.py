class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x \
        and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False

    def calculate_distance(self, point):
        return ((point.x - self.x)**2 + \
                (point.y - self.y)**2)**1/2

class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def calculate_the_area(self):
        return (self.upright.x - self.lowleft.x) * \
                (self.upright.y - self.lowleft.y)