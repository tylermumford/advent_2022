package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("Starting...")

	file, err := ioutil.ReadFile("input")
	if err != nil {
		panic(err)
	}

	input := string(file)

	answer := calculateAnswer(input)
	fmt.Println("Part 1: The elf with the most calories has", answer.part1, "calories.")
	fmt.Println("Part 2: The sum of the three highest-calorie elves is", answer.part2)
}

type answer struct {
	part1 int
	part2 int
}

func calculateAnswer(input string) answer {
	elves := convertIntoElves(input)

	fmt.Println("Loaded", len(elves), "elves")

	answer := answer{}

	answer.part1 = findHighestCalorieTotal(elves)
	answer.part2 = findSumOfThreeHighestTotals(elves)

	return answer
}

type elf struct {
	itemCalories []int
	calorieTotal int
}

func convertIntoElves(input string) []elf {
	groups := strings.Split(input, "\n\n")

	elves := make([]elf, 0, len(groups))

	for _, group := range groups {
		lines := strings.Split(group, "\n")

		nextElf := elf{}

		for _, line := range lines {
			if line == "" {
				continue
			}

			n, err := strconv.Atoi(line)
			if err != nil {
				panic(err)
			}

			nextElf.itemCalories = append(nextElf.itemCalories, n)
			nextElf.calorieTotal += n
		}

		elves = append(elves, nextElf)
	}

	return elves
}

func findHighestCalorieTotal(elves []elf) int {
	highest := 0

	for _, elf := range elves {
		if elf.calorieTotal > highest {
			highest = elf.calorieTotal
		}
	}

	return highest
}

func findSumOfThreeHighestTotals(elves []elf) int {
	var first, second, third int

	for _, elf := range elves {
		total := elf.calorieTotal

		if total >= first {
			third = second
			second = first
			first = total
		} else if total >= second {
			third = second
			second = total
		} else if total > third {
			third = total
		}
	}

	fmt.Println("First:", first, "Second:", second, "Third:", third)

	return first + second + third
}
