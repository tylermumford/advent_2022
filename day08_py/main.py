from forest import Forest

def main(file):
    f = Forest()
    with open(file, encoding="utf-8") as data:
        f.parse(data)

    f.analyze()

    print(file)
    print("Visible count:", f.count_visible())
    print("Highest scenic score:", f.max_scenic_score(), "\n")
    print(str(f))

if __name__ == '__main__':
    main('sample.txt')
    main('myinput.txt')

