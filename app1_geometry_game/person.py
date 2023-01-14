class Person:
    def __init__(self, name, velocity, *start_x):
        self.name = name
        self.velocity = velocity
        self.start_x = start_x

    def start_run(self):
        ...