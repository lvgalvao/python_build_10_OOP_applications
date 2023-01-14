class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printer(self):
        return print(self.x, self.y)

class Rectangule:
    def __init__(self, x: Point, y):
        self.x = x
        self.y = y
