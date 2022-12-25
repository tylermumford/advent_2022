import unittest
from rope import *
from direction import Direction
from command import Command
import logging

logging.basicConfig(level=logging.WARNING)

class RunTests(unittest.TestCase):
    def test_NoMovement(self):
        r = Rope()

        r.run([])

        # The tail starts somewhere, and that counts
        self.assertEqual(r.distinctTailPositions, 1)

    def test_RightTwo(self):
        r = Rope()

        r.run([Command('R', 2)])

        self.assertEqual(r.distinctTailPositions, 2)

    def test_DownTwo(self):
        r = Rope()

        r.run([Command('D', 2)])

        self.assertEqual(r.distinctTailPositions, 2)

    def test_UpTwo(self):
        r = Rope()

        r.run([Command('U', 2)])

        self.assertEqual(r.distinctTailPositions, 2)

    def test_LeftTwo(self):
        r = Rope()

        r.run([Command('L', 2)])

        self.assertEqual(r.distinctTailPositions, 2)

    def test_LeftThree(self):
        r = Rope()

        r.run([Command('L', 3)])

        self.assertEqual(r.distinctTailPositions, 3)

    def test_UpThree(self):
        r = Rope()

        r.run([Command('U', 3)])

        self.assertEqual(r.distinctTailPositions, 3)

    def test_TwoDirections(self):
        r = Rope()

        r.run([Command('U', 3), Command('R', 2)])

        self.assertEqual(r.distinctTailPositions, 4)

    def test_mv(self):
        self.assertEqual(mv((0, 0), Direction.RIGHT), (1, 0))
        self.assertEqual(mv((0, 0), Direction.LEFT), (-1, 0))
        self.assertEqual(mv((0, 0), Direction.UP), (0, 1))
        self.assertEqual(mv((0, 0), Direction.DOWN), (0, -1))

    def test_dist(self):
        d1 = dist((0,0), (1,0))
        d2 = dist((0,0), (2,0))

        self.assertEqual(d1, 1)
        self.assertEqual(d2, 2)

if __name__ == '__main__':
    unittest.main()
