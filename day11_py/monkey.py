class Monkey:
    def __init__(self):
        self.id = 0
        self.inspectionCount = 0
        self.operation = lambda : None
        self.test = lambda : None
        self.trueThrowTo = 0
        self.falseThrowTo = 0
        self.items = []

    def __repr__(self):
        return (
                f"Monkey {str(self.id)}: "
                + f"inspected {str(self.inspectionCount):8} times, "
                + f"holding {str(self.items)}"
        )

    def turn(self, allMonkeys):
        pass

