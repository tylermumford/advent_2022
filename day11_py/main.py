import monkey
from pprint import pp
#from setup import Monkeys
from setup_sample import Monkeys

def main():
    performRounds(20)

    print(monkeyBusiness())

def performRounds(count):
    for i in range(0, count):
        print(f"=== Round {i+1} ===")
        allMonkeysTakeATurn()

def allMonkeysTakeATurn():
    for id in Monkeys:
        Monkeys[id].turn(Monkeys)

    pp(Monkeys)

def monkeyBusiness():
    allMonkeys = [m for m in Monkeys]
    byActivity = sorted(Monkeys.values(), key=lambda m: m.inspectionCount, reverse=True)
    topTwo = byActivity[0:2]
    inspections = [m.inspectionCount for m in topTwo]
    return inspections[0] * inspections[1]

if __name__ == "__main__":
    main()
