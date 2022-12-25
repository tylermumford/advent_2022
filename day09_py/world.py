class World():
    def __init__(self, visible=False):
        self.distinctTailPositions = 1
        self.visible = visible

    def run(self, commands):
        self._p(commands)


    def _p(self, args):
        if self.visible:
            print(args)
