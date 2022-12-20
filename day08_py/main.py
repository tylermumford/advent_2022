from forest import Forest

def main(file):
    f = Forest()
    with open(file, encoding="utf-8") as data:
        f.parse(data)

    f.analyze()

    print("Visible count:", f.count_visible(), "\n")
    print(str(f))

if __name__ == '__main__':
    main('sample.txt')
    main('myinput.txt')

