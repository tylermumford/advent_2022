import logging
from direction import Direction

class World():
    def __init__(self, visible=False):
        self.visible = visible

        self.head = (0,0)
        self.tail = (0,0)

        self.visited = set((0,0))

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

    def stepTail(self):
        gap = dist(self.head, self.tail)
        logging.debug(f"gap is {gap}")

        if gap > 1:
            self.catchUp()

    def catchUp(self):
        dx = distx(self.tail, self.head)
        x = self.tail[0] + (1 if dx > 1 else 0)
        self.tail = (x, self.tail[1])

        # TODO: dy, y
        self.visited.add(self.tail)

    def _p(self, args):
        if self.visible:
            print(args)

def mv(pair, direction):
    'Move the coordinates in `pair` one step in the `direction` given.'
    if direction == Direction.RIGHT:
        return pair[0] + 1, pair[1]

    raise f"{direction} not supported by mv function"
    # TODO: More directions

def dist(pair1, pair2):
    horiz = abs(pair1[0] - pair2[0])
    vert = abs(pair1[1] - pair2[1])
    return max(horiz, vert)

def distx(pair1, pair2):
    return pair2[0] - pair1[0]

def disty(pair1, pair2):
    return pair2[1] - pair1[1]
