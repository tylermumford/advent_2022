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

    def scenic_str(self):
        result = []

        for line in self.trees:
            for t in line:
                result.append(str(t.scenic_score) + '\t')

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
        """Determine whether t is hidden or visible, and set its scenic score."""
        # Remember that Trees are visible by default.
        if self.is_on_edge(t):
            t.hidden = False
            t.scenic_score = 0
            return

        self.set_scenic_score(t)

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
        """Primary logic of part 1.

        A tree is visible from a given direction if
        the other trees on the way to the edge of the
        forest are stricly smaller than the subject
        tree."""

        n = direction.step

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

    def set_scenic_score(self, t):
        score = 1

        for direction in list(Direction):
            score *= self.calculate_scenic_score(t, direction)

        t.scenic_score = score

    def calculate_scenic_score(self, t, direction):
        """Primary logic of part 2."""
        nextLine, nextCol = t.line, t.col

        visible_count = 0

        while True:
            # Continue visiting trees in the direction given
            nextLine, nextCol = direction.step(nextLine, nextCol)
            if self.is_out_of_range(nextLine, nextCol):
                break

            distant_tree = self.trees[nextLine][nextCol]
            visible_count += 1

            if distant_tree.height < t.height:
                continue
            else:
                break

        return visible_count

    def max_scenic_score(self):
        return max([t.scenic_score for t in self.all_trees()])

