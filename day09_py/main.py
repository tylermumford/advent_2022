import logging
from world import World
from command import Command

def main():
    print("Sample:")
    sample = World(visible=True)
    sample.run(cmds('sample-input.txt'))
    print(f"Tail positions: {sample.distinctTailPositions}")

    print('\nMain input:')
    inputt = World()
    inputt.run(cmds('main-input.txt'))
    print(f"Tail positions: {inputt.distinctTailPositions}")

def cmds(filename):
    lines = []
    with open(filename) as f:
        for l in f:
            cmd = Command(l[0], int(l.split()[1]))
            logging.debug(f"Parsed command {str(cmd)}")
            lines.append(cmd)
    return lines

if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)
    main()
