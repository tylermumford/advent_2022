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

    def count_visible(self):
        count = 0
        for line in self.trees:
            for t in line:
                if t.hidden:
                    count = count + 1
        return count
        
    def analyze(self):
        for line in self.trees:
            for t in line:
                self.analyzeTree(t)

    def analyzeTree(self, t):
        """Determine whether t is hidden or visible."""

        pass
