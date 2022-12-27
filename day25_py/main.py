import convert
import pprint

def main():
    print("AoC 2022: Day 25\n")

    do("sample.txt", visible=True)
    print()
    do("input.txt")

def do(filename, visible=False):
    print(filename)

    lines = []
    with open(filename) as file:
        for l in file:
            lines.append(l.strip())

    print(len(lines), "lines")

    mapping = convertToDecimal(lines)
    if visible: pprint.pp(mapping)

    decimals = [pair[1] for pair in mapping]
    total = sum(decimals)
    print("Total:", total)

    snafuTotal = convert.toSnafu(total)
    print("Total (SNAFU):", snafuTotal)

def convertToDecimal(lines):
    decimalLines = [convert.toDecimal(line) for line in lines]
    return list(zip(lines, decimalLines))

if __name__ == "__main__":
    main()
