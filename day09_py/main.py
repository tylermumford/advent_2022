from world import World
from command import Command

def main():
    print("Sample:")
    sample = World(visible=True)
    sample.run(cmds('sample-input.txt'))
    print(f"Tail positions: {sample.distinctTailPositions}")

def cmds(filename):
    lines = []
    with open(filename) as f:
        for l in f:
            cmd = Command(l[0], l.split()[1])
            lines.append(str(cmd))
    return lines

if __name__ == '__main__':
    main()
