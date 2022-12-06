package main

import (
	"fmt"
)

func main() {
	loadInputs()

	fmt.Println("Sample has", len(inputs.sample), "lines, and main input has", len(inputs.input))

	fmt.Println("Sample input:")
	printFullOverlapCount(inputs.sample)
	printOverlapCount(inputs.sample)

	fmt.Println()

	fmt.Println("Main input:")
	printFullOverlapCount(inputs.input)
	printOverlapCount(inputs.input)
}

func printFullOverlapCount(pairs []pair) {
	count := 0

	for _, p := range pairs {
		if p.hasFullOverlap() {
			count++
		}
	}

	fmt.Println(count, "pairs with a full overlap")
}

func (p pair) hasFullOverlap() bool {
	return p.first.fullyContains(p.second) || p.second.fullyContains(p.first)
}

func (p pair) hasAnyOverlap() bool {
	return p.first.overlapsWith(p.second)
}

func (s span) fullyContains(other span) bool {
	if other.from < s.from || other.to > s.to {
		return false
	}

	return true
}

func (s span) overlapsWith(other span) bool {
	hasBottomOverlap := (s.from <= other.from) && (other.from <= s.to)
	hasTopOverlap := (s.from <= other.to) && (other.to <= s.to)

	return hasBottomOverlap || hasTopOverlap
}

func printOverlapCount(pairs []pair) {
	count := 0

	for _, p := range pairs {
		if p.hasAnyOverlap() {
			count++
		}
	}

	fmt.Println(count, "pairs with ANY overlap")
}
