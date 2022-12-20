from tree import Tree
from direction import Direction

class Forest:
    def __init__(self):
        self.trees = []

    def __str__(self):
        result = []

        for line in self.trees:
            for t in line:
                result.append(str(t))

            result.append('\n')

        return "".join(result)

    def parse(self, data):
        for l, line in enumerate(data):
            treeRow = []
            for col, ch in enumerate(line):
                if ch != '\n':
                    treeRow.append(Tree(ch, l, col))
            self.trees.append(treeRow)

    def all_trees(self):
        for line in self.trees:
            for t in line:
                yield t

    def count_visible(self):
        count = len([None for t in self.all_trees() if not t.hidden])
        return count

    def analyze(self):
        for t in self.all_trees():
            self.analyzeTree(t)

    def analyzeTree(self, t):
        """Determine whether t is hidden or visible."""
        # Remember that Trees are visible by default.
        if self.is_on_edge(t):
            t.hidden = False
            return

        is_totally_hidden = True
        for direction in list(Direction):
            if self.is_visible(direction, t):
                t.hidden = False
                return

        t.hidden = True

    def is_on_edge(self, t):
        top = t.line == 0
        bottom = t.line == len(self.trees[0]) - 1
        left = t.col == 0
        right = t.col == len(self.trees) - 1

        return top or bottom or left or right

    def is_visible(self, direction, t):
        """Primary logic of the program.

        A tree is visible from a given direction if
        the other trees on the way to the edge of the
        forest are stricly smaller than the subject
        tree."""

        if direction is Direction.EAST:
            n = lambda line, col: (line, col + 1)
        elif direction is Direction.WEST:
            n = lambda line, col: (line, col - 1)
        elif direction is Direction.NORTH:
            n = lambda line, col: (line - 1, col)
        elif direction is Direction.SOUTH:
            n = lambda line, col: (line + 1, col)
        else:
            return False

        nextLine, nextCol = t.line, t.col

        while True:
            nextLine, nextCol = n(nextLine, nextCol)
            if self.is_out_of_range(nextLine, nextCol):
                return True

            nextTree = self.trees[nextLine][nextCol]

            if nextTree.height >= t.height:
                return False
        pass

    def is_out_of_range(self, line, col):
        if line < 0 or line >= len(self.trees):
            return True

        if col < 0 or col >= len(self.trees[0]):
            return True

        return False
