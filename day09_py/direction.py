from enum import Enum, auto

class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

def toDirection(char):
    if char == 'U':
        return Direction.UP
    if char == 'D':
        return Direction.DOWN
    if char == 'L':
        return Direction.LEFT
    if char == 'R':
        return Direction.RIGHT

    raise f"Unknown direction: '{char}'"

