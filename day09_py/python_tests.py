import unittest

class PythonTests(unittest.TestCase):
    def test_TuplesInSets(self):
        s = set([(0,0)])
        s.add((0,0))
        s.add((0,0))

        self.assertEqual(len(s), 1)
        # From this test, I learned that set((0,0))
        # creates a set with one element, 0, NOT a set
        # with one tuple element.

    def test_TupleEquality(self):
        a = (5, 6)
        b = (5, 6)

        self.assertEqual(a, b)
        self.assertTrue(a == b)

