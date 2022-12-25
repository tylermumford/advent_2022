from direction import *

class Command():
    def __init__(self, direction, steps):
        self.direction = toDirection(direction)
        self.steps = steps

    def __str__(self):
        return f"{str(self.direction)} {self.steps} steps"
