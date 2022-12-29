from monkey import Monkey
import pprint
import math
import functools

Monkeys = dict()

def _setup():
    m = Monkey(0)
    m.items = [91, 66]
    m.operation = lambda x: x * 13
    m.divisor = 19
    m.trueThrowTo = 6
    m.falseThrowTo = 2
    Monkeys[0] = m

    m = Monkey(1)
    m.items = [78, 97, 59]
    m.operation = lambda x: x + 7
    m.divisor = 5
    m.trueThrowTo = 0
    m.falseThrowTo = 3
    Monkeys[1] = m

    m = Monkey(2)
    m.items = [57, 59, 97, 84, 72, 83, 56, 76]
    m.operation = lambda x: x + 6
    m.divisor = 11
    m.trueThrowTo = 5
    m.falseThrowTo = 7
    Monkeys[2] = m


    m = Monkey(3)
    m.items = [81, 78, 70, 58, 84]
    m.operation = lambda x: x + 5
    m.divisor = 17
    m.trueThrowTo = 6
    m.falseThrowTo = 0
    Monkeys[3] = m

    m = Monkey(4)
    m.items = [60]
    m.operation = lambda x: x + 8
    m.divisor = 7
    m.trueThrowTo = 1
    m.falseThrowTo = 3
    Monkeys[4] = m

    m = Monkey(5)
    m.items = [57, 69, 63, 75, 62, 77, 72]
    m.operation = lambda x: x * 5
    m.divisor = 13
    m.trueThrowTo = 7
    m.falseThrowTo = 4
    Monkeys[5] = m

    m = Monkey(6)
    m.items = [73, 66, 86, 79, 98, 87]
    m.operation = lambda x: x * x
    m.divisor = 3
    m.trueThrowTo = 5
    m.falseThrowTo = 2
    Monkeys[6] = m

    m = Monkey(7)
    m.items = [95, 89, 63, 67]
    m.operation = lambda x: x + 2
    m.divisor = 2
    m.trueThrowTo = 1
    m.falseThrowTo = 4
    Monkeys[7] = m

    _setModuland()

def _setModuland():
    divisors = [m.divisor for m in Monkeys.values()]
    lcm = math.lcm(*divisors)
    for m in Monkeys.values():
        m.moduland = lcm

_setup()

if __name__ == "__main__":
    pprint.pp(Monkeys)
