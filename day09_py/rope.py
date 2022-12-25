import logging
from direction import Direction

class Rope():
    def __init__(self, visible=False):
        self.visible = visible

        self.head = (0,0)
        self.tail = (0,0)

        self.visited = set([(0,0)])

    @property
    def distinctTailPositions(self):
        return len(self.visited)

    def run(self, commands):
        logging.debug(f"Running {len(commands)} commands")

        for c in commands:
            logging.debug(f"Running command {c}")

            self.runCommand(c)

    def runCommand(self, c):
        for i in range(0, c.steps):
            self.step(c.direction)

    def step(self, direction):
        logging.debug(f"Moving one to the {direction}")

        self.head = mv(self.head, direction)
        self.stepTail()

        self._draw()

    def stepTail(self):
        gap = dist(self.head, self.tail)
        logging.debug(f"gap is {gap}")

        if gap > 1:
            self.catchUp()

    def catchUp(self):
        logging.debug("catching up")
        startValue = self.tail

        dx = distx(self.tail, self.head)
        dx = abs(dx) / (dx if dx != 0 else 1)
        x = self.tail[0] + dx

        dy = disty(self.tail, self.head)
        dy = abs(dy) / (dy if dy != 0 else 1)
        y = self.tail[1] + dy

        self.tail = (x, y)

        newValue = self.tail
        logging.debug(f"caught up by moving from {startValue} to {newValue}")

        self.visited.add(self.tail)

    def _draw(self):
        if not self.visible:
            return

        image = []

        for y in range(9, -2, -1):
            for x in range(-2, 9):
                point = '.'
                if (x,y) in self.visited: point = '#'
                if (x,y) == self.tail: point = 'T'
                if (x,y) == self.head: point = 'H'
                image.append(point)
            image.append('\n')

        print(''.join(image))

    def _p(self, args):
        if self.visible:
            print(args)

def mv(pair, direction):
    'Move the coordinates in `pair` one step in the `direction` given.'
    if direction == Direction.RIGHT:
        return pair[0] + 1, pair[1]
    if direction == Direction.LEFT:
        return pair[0] - 1, pair[1]
    if direction == Direction.UP:
        return pair[0], pair[1] + 1
    if direction == Direction.DOWN:
        return pair[0], pair[1] - 1

    raise NotImplementedError(f"{direction} not supported by mv function")

def dist(pair1, pair2):
    horiz = abs(pair1[0] - pair2[0])
    vert = abs(pair1[1] - pair2[1])
    return max(horiz, vert)

def distx(pair1, pair2):
    return pair2[0] - pair1[0]

def disty(pair1, pair2):
    return pair2[1] - pair1[1]
