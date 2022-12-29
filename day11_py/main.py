import monkey
from pprint import pp
from setup import Monkeys
from setup_sample import Monkeys as SampleMonkeys

def main():
    performRounds(20, SampleMonkeys)

    business = monkeyBusiness(SampleMonkeys)
    print("Monkey business:", business)

    assert business in [10605, 101436, 2713310158], \
        f"Monkey business was an unexpected {business}"

def performRounds(count, monkeyGroup):
    for i in range(0, count):
        print(f"=== Round {i+1} ===")
        allMonkeysTakeATurn(monkeyGroup)

def allMonkeysTakeATurn(monkeyGroup):
    for id in monkeyGroup:
        monkeyGroup[id].turn(monkeyGroup)

    pp(monkeyGroup)

def monkeyBusiness(monkeyGroup):
    allMonkeys = [m for m in monkeyGroup]
    byActivity = sorted(
            monkeyGroup.values(),
            key=lambda m: m.inspectionCount,
            reverse=True)
    topTwo = byActivity[0:2]
    inspections = [m.inspectionCount for m in topTwo]
    return inspections[0] * inspections[1]

if __name__ == "__main__":
    main()
