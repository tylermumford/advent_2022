from tree import Tree

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
        pass

    def is_on_edge(self, t):
        top = t.line == 0
        bottom = t.line == len(self.trees[0]) - 1
        left = t.col == 0
        right = t.col == len(self.trees) - 1

        return top or bottom or left or right
