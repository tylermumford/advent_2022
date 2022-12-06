package main

import (
	"os"
	"strconv"
	"strings"
)

var inputs struct {
	sample []pair
	input  []pair
}

type pair struct {
	first  span
	second span
}

type span struct {
	from int
	to   int
}

func loadInputs() {
	rawSample, err := os.ReadFile("sampleInput")
	if err != nil {
		panic(err)
	}

	lines := strings.Split(strings.TrimSpace(string(rawSample)), "\n")
	inputs.sample = linesToPairs(lines)

	rawInput, err := os.ReadFile("input")
	if err != nil {
		panic(err)
	}

	lines = strings.Split(strings.TrimSpace(string(rawInput)), "\n")
	inputs.input = linesToPairs(lines)
}

func linesToPairs(lines []string) []pair {
	pairs := make([]pair, 0, len(lines))

	for _, line := range lines {
		pairs = append(pairs, lineToPair(line))
	}

	return pairs
}

func lineToPair(line string) pair {
	parts := strings.Split(line, ",")
	left := parts[0]
	right := parts[1]

	return pair{
		first:  parseSpan(left),
		second: parseSpan(right),
	}
}

// input looks like "4-18"
func parseSpan(input string) span {
	sides := strings.Split(input, "-")

	a, _ := strconv.Atoi(sides[0])
	b, _ := strconv.Atoi(sides[1])

	return span{
		from: a,
		to:   b,
	}
}
