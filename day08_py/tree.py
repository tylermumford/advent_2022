class Tree:
    def __init__(self, height, line=0, col=0):
        self.height = height
        self.line = line
        self.col = col
        self.hidden = False

    def __str__(self):
        return str(self.height) if not self.hidden else "h"

    def debugstr(self):
        return f"(Tree:h{self.height}:line{self.line}:col{self.col})"
