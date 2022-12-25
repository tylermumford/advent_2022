import unittest
from world import World
from direction import Direction
from command import Command

class ExpressionTests(unittest.TestCase):

    # Tests about the world

    def test_canCreateAWorld(self):
        World()

    def test_canSendInputToWorld(self):
        data = []
        w = World()
        w.run(data)

    def test_canGetTailVisits(self):
        w = World()
        w.run([])
        0 <= w.distinctTailPositions

    def test_canTellWorldToShowItsWork(self):
        World(visible=True)

    # Tests about commands

    def test_canNameDirections(self):
        Direction.UP
        Direction.DOWN
        Direction.LEFT
        Direction.RIGHT

    def test_canWriteACommand(self):
        Command('R', 7)
        Command('U', 3)

if __name__ == '__main__':
    unittest.main()
