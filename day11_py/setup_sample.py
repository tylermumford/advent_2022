from monkey import Monkey
import pprint

Monkeys = dict()

def _setup():
    m = Monkey(0)
    m.items = [79, 98]
    m.operation = lambda x: x * 19
    m.divisor = 23
    m.trueThrowTo = 2
    m.falseThrowTo = 3
    Monkeys[0] = m

    m = Monkey(1)
    m.items = [54, 65, 75, 74]
    m.operation = lambda x: x + 6
    m.divisor = 19
    m.trueThrowTo = 2
    m.falseThrowTo = 0
    Monkeys[1] = m

    m = Monkey(2)
    m.items = [79, 60, 97]
    m.operation = lambda x: x * x
    m.divisor = 13
    m.trueThrowTo = 1
    m.falseThrowTo = 3
    Monkeys[2] = m


    m = Monkey(3)
    m.items = [74]
    m.operation = lambda x: x + 3
    m.divisor = 17
    m.trueThrowTo = 0
    m.falseThrowTo = 1
    Monkeys[3] = m

_setup()

if __name__ == "__main__":
    pprint.pp(Monkeys)
