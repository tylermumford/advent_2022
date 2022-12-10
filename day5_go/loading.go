package main

import (
	"os"
	"regexp"
	"strconv"
	"strings"
)

var inputs struct {
	sample domain
	real   domain
}

func loadInputs() {
	inputs.sample = load("sampleInput.txt")
	inputs.real = load("input.txt")
}

func load(filename string) domain {
	rawBytes, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}

	file := string(rawBytes)

	return fileToDomain(file)
}

func fileToDomain(file string) domain {
	sections := strings.Split(file, "\n\n")

	d := domain{
		ship:     parseShip(sections[0]),
		commands: parseCommands(sections[1]),

		ship9001: parseShip(sections[0]),
	}

	d.ship9001.isCrateMover9001(true)

	return d
}

func parseShip(input string) ship {
	trimmed := strings.TrimRight(input, "\n \t")
	lines := strings.Split(trimmed, "\n")

	// We're going to iterate through the lines
	// from bottom to top.
	i := len(lines) - 1

	lastLine := lines[i]
	indexes := inferIndexes(lastLine)
	i--

	ship := NewShip(len(indexes))

	for ; i >= 0; i-- {
		line := lines[i]

		for j, idx := range indexes {
			if idx >= len(line) {
				continue
			}

			var c crate = crate(line[idx])
			if c == " " {
				continue
			}

			ship.AddCrate(c, stackId(j))
		}
	}

	return ship

}

// input is like " 1   2   3"; returns the indices of
// the numbers.
// Assumes that each number is only a *single digit.*
func inferIndexes(line string) []int {
	// The first one is always at index 1
	indexes := []int{1}

	// There are three spaces and one digit between,
	// so the next possible one is at index 5
	i := 5

	for i < len(line) {
		indexes = append(indexes, i)
		i += 4
	}

	return indexes
}

func parseCommands(input string) commands {
	lines := strings.Split(strings.TrimSpace(input), "\n")
	result := make(commands, 0, len(lines))

	for _, line := range lines {
		c := parseCommand(line)
		result = append(result, c)
	}

	return result
}

var commandRegex, _ = regexp.Compile(`move (\d+) from (\d+) to (\d+)`)

func parseCommand(input string) command {
	m := commandRegex.FindStringSubmatch(input)

	count, _ := strconv.Atoi(m[1])
	from, _ := strconv.Atoi(m[2])
	to, _ := strconv.Atoi(m[3])

	return command{
		n:    count,
		from: stackId(from),
		to:   stackId(to),
	}
}
