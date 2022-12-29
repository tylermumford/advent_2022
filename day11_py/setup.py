from monkey import Monkey
import pprint

Monkeys = dict()

def _setup():
    m = Monkey()
    m.id = 0
    m.items = [91, 66]
    m.operation = lambda x: x * 13
    m.test = lambda x: x % 19 == 0
    m.trueThrowTo = 6
    m.falseThrowTo = 2
    Monkeys[0] = m

    m = Monkey()
    m.id = 1
    m.items = [78, 97, 59]
    m.operation = lambda x: x + 7
    m.test = lambda x: x % 5 == 0
    m.trueThrowTo = 0
    m.falseThrowTo = 3
    Monkeys[1] = m

    m = Monkey()
    m.id = 2
    m.items = [57, 59, 97, 84, 72, 83, 56, 76]
    m.operation = lambda x: x + 6
    m.test = lambda x: x % 11 == 0
    m.trueThrowTo = 5
    m.falseThrowTo = 7
    Monkeys[2] = m


    m = Monkey()
    m.id = 3
    m.items = [81, 78, 70, 58, 84]
    m.operation = lambda x: x + 5
    m.test = lambda x: x % 17 == 0
    m.trueThrowTo = 6
    m.falseThrowTo = 0
    Monkeys[3] = m

    m = Monkey()
    m.id = 4
    m.items = [60]
    m.operation = lambda x: x + 8
    m.test = lambda x: x % 9 == 0
    m.trueThrowTo = 1
    m.falseThrowTo = 3
    Monkeys[4] = m

    m = Monkey()
    m.id = 5
    m.items = [57, 69, 63, 75, 62, 77, 72]
    m.operation = lambda x: x * 5
    m.test = lambda x: x % 13 == 0
    m.trueThrowTo = 7
    m.falseThrowTo = 4
    Monkeys[5] = m

    m = Monkey()
    m.id = 6
    m.items = [73, 66, 86, 79, 98, 87]
    m.operation = lambda x: x * x
    m.test = lambda x: x % 3 == 0
    m.trueThrowTo = 5
    m.falseThrowTo = 2
    Monkeys[6] = m

    m = Monkey()
    m.id = 7
    m.items = [95, 89, 63, 67]
    m.operation = lambda x: x + 2
    m.test = lambda x: x % 2 == 0
    m.trueThrowTo = 1
    m.falseThrowTo = 4
    Monkeys[7] = m
_setup()

if __name__ == "__main__":
    pprint.pp(Monkeys)
