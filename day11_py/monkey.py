import logging

_level = logging.WARNING

class Monkey:
    def __init__(self, id):
        self.id = id
        self.inspectionCount = 0
        self.operation = lambda : None
        self.test = lambda : None
        self.trueThrowTo = 0
        self.falseThrowTo = 0
        self.items = []

        self.logger = logging.getLogger(__name__)

    def __repr__(self):
        return (
                f"Monkey {str(self.id)}: "
                + f"inspected {str(self.inspectionCount):8} times, "
                + f"holding {str(self.items)}"
        )

    def log(self, msg):
        self.logger.log(_level, f"M{self.id} {msg}")

    # On a monkey's turn:
    # For EACH item it's holding:
    # 1. It inspects the item, which adjusts its worry level
    #    according to that monkey's *operation*
    # 2. You are relieved, which divides the worry level by 3
    # 3. The monkey uses *test* to decide where to throw the item
    def turn(self, allMonkeys):
        self.log("Taking a turn")

        if len(self.items) == 0:
            self.log("Holding no items. Turn over.")
            return

        while len(self.items) > 0:
            # Inspect
            self.items[0] = self.operation(self.items[0])
            self.inspectionCount += 1

            # Relief
            self.items[0] = self.items[0] // 3

            # Test and throw
            hmm = self.test(self.items[0])
            if hmm == True:
                catcher = self.trueThrowTo
            elif hmm == False:
                catcher = self.falseThrowTo

            allMonkeys[catcher].catch(self.items[0])

            del self.items[0]

    def catch(self, number):
        self.items.append(number)
