import unittest
from world import World

class RunTests(unittest.TestCase):
    def test_NoMovement(self):
        w = World()

        w.run([])

        # The tail starts somewhere, and that counts
        self.assertEqual(w.distinctTailPositions, 1)
