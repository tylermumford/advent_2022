import monkey
from pprint import pp
from setup import Monkeys


def main():
    performRounds(20)

    print(monkeyBusiness())

def performRounds(count):
    for i in range(0, count):
        allMonkeysTakeATurn()

def allMonkeysTakeATurn():
    for id in Monkeys:
        Monkeys[id].turn(Monkeys)

    pp(Monkeys)

def monkeyBusiness():
    allMonkeys = [m for m in Monkeys]
    byActivity = sorted(Monkeys.values(), key=lambda m: m.inspectionCount, reverse=True)
    topTwo = byActivity[0:2]
    return sum([m.inspectionCount for m in topTwo])

if __name__ == "__main__":
    main()
