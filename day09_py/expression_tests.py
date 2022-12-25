import unittest
from rope import Rope
from direction import Direction
from command import Command

class ExpressionTests(unittest.TestCase):

    # Tests about ropes

    def test_canCreateARope(self):
        Rope()

    def test_canSendInputToRope(self):
        data = []
        r = Rope()
        r.run(data)

    def test_canGetTailVisits(self):
        r = Rope()
        r.run([])
        0 <= r.distinctTailPositions

    def test_canTellRopeToShowItsWork(self):
        Rope(visible=True)

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
