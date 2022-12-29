import monkey
import copy
from pprint import pp
from setup import Monkeys
from setup_sample import Monkeys as SampleMonkeys

def main():
    # It's important to work with a copy (at least one), otherwise
    # the monkeys carry over their inspection counts.
    p1Sample = copy.deepcopy(SampleMonkeys)
    performRounds(20, p1Sample)
    showMonkeyBusiness(p1Sample, expected=10605)

    p1MyInput = copy.deepcopy(Monkeys)
    performRounds(20, p1MyInput)
    showMonkeyBusiness(p1MyInput, expected=101436)

    # Flip the toggle that enables Part 2 behavior
    p2Sample = copy.deepcopy(SampleMonkeys)
    p2MyInput = copy.deepcopy(Monkeys)
    flipToggle(p2Sample)
    flipToggle(p2MyInput)

    performRounds(10000, p2Sample)
    showMonkeyBusiness(p2Sample, expected=2713310158)

    performRounds(10000, p2MyInput)
    showMonkeyBusiness(p2MyInput, expected=19754471646)

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
