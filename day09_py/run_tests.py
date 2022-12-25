import unittest
from world import *
from direction import Direction
from command import Command
import logging

logging.basicConfig(level=logging.WARNING)

class RunTests(unittest.TestCase):
    def test_NoMovement(self):
        w = World()

        w.run([])

        # The tail starts somewhere, and that counts
        self.assertEqual(w.distinctTailPositions, 1)

    def test_RightTwo(self):
        w = World(visible=True)

        w.run([Command('R', 2)])

        self.assertEqual(w.distinctTailPositions, 2)

    def test_mv(self):
        self.assertEqual(mv((0, 0), Direction.RIGHT), (1, 0))

    def test_dist(self):
        d1 = dist((0,0), (1,0))
        d2 = dist((0,0), (2,0))

        self.assertEqual(d1, 1)
        self.assertEqual(d2, 2)

if __name__ == '__main__':
    unittest.main()
