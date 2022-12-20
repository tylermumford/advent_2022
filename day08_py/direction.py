from enum import Enum, auto

class Direction(Enum):
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()

    def step(self, line, col):
        if self is Direction.EAST:
            return line, col + 1

        elif self is Direction.WEST:
            return line, col - 1

        elif self is Direction.NORTH:
            return line - 1, col

        elif self is Direction.SOUTH:
            return line + 1, col

        else:
            raise f"Undefined direction '{self}'"
