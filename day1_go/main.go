package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("Starting...")

	file, err := ioutil.ReadFile("sampleInput")
	if err != nil {
		panic(err)
	}

	input := string(file)

	answer := calculateAnswer(input)
	fmt.Println("Answer: The elf with the most calories has", answer, "calories.")
}

func calculateAnswer(input string) int {
	answer := 0

	elves := convertIntoElves(input)

	fmt.Println("Loaded", len(elves), "elves")

	answer = findHighestCalorieTotal(elves)

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
