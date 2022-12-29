import monkey
from pprint import pp
from setup import Monkeys
from setup_sample import Monkeys as SampleMonkeys

def main():
    performRounds(20, SampleMonkeys)
    showMonkeyBusiness(SampleMonkeys, expected=10605)

    performRounds(20, Monkeys)
    showMonkeyBusiness(Monkeys, expected=101436)

    # Flip the toggle that enables Part 2 behavior
    flipToggle(SampleMonkeys)
    flipToggle(Monkeys)

    performRounds(10000, SampleMonkeys)
    showMonkeyBusiness(SampleMonkeys, expected=2713310158)

def performRounds(count, monkeyGroup):
    for i in range(0, count):
        if i in [0, 19, 9999]: print(f"=== Round {i+1} ===")
        allMonkeysTakeATurn(monkeyGroup)
        if i in [0, 19, 9999]: pp(monkeyGroup)

def allMonkeysTakeATurn(monkeyGroup):
    for id in monkeyGroup:
        monkeyGroup[id].turn(monkeyGroup)

def showMonkeyBusiness(monkeyGroup, expected=None, atLeast=None):
    byInspections = sorted(
            monkeyGroup.values(),
            key=lambda m: m.inspectionCount,
            reverse=True)
    topTwo = byInspections[0:2]
    inspections = [m.inspectionCount for m in topTwo]
    business = inspections[0] * inspections[1]

    print("Monkey business:", business)

    if expected:
        assert business == expected, "Expected " + str(expected)

    if atLeast:
        assert business > atLeast, "That number is definitely too low."

def flipToggle(monkeyGroup):
    for id in monkeyGroup:
        monkeyGroup[id].canDivideByThree = False

if __name__ == "__main__":
    main()
