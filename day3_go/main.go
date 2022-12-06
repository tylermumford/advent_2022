package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	loadInputs()

	fmt.Println("Sample has", len(inputs.sample), "lines, and main input has", len(inputs.input))

	fmt.Println("Sample input:")
	printPrioritySum(inputs.sample)

	fmt.Println()

	fmt.Println("Main input:")
	printPrioritySum(inputs.input)
}

var inputs struct {
	sample []string
	input  []string
}

func loadInputs() {
	rawSample, err := os.ReadFile("sampleInput")
	if err != nil {
		panic(err)
	}

	inputs.sample = strings.Split(strings.TrimSpace(string(rawSample)), "\n")

	rawInput, err := os.ReadFile("input")
	if err != nil {
		panic(err)
	}

	inputs.input = strings.Split(strings.TrimSpace(string(rawInput)), "\n")
}

func printPrioritySum(input []string) {
	prioritySum := 0

	for _, str := range input {
		itemCode := itemInCommon(str)
		prioritySum += priority(itemCode)
	}

	fmt.Println("Priority sum =", prioritySum)
}

func itemInCommon(str string) rune {
	length := len(str)
	subLength := length / 2

	firstCompartment := str[0:subLength]
	secondCompartment := str[subLength:]

	if len(firstCompartment) != len(secondCompartment) {
		panic("You messed up here")
	}

	for _, c := range firstCompartment {
		if strings.ContainsRune(secondCompartment, c) {
			return c
		}
	}

	panic("There's supposed to be something in common here.")
}

func priority(c rune) int {
	// 'a' is defined as 1
	isLowercase := c >= 'a' && c <= 'z'
	isUppercase := c >= 'A' && c <= 'Z'

	if isLowercase {
		const offset = 1 - 'a'
		return int(c + offset)
	}

	if isUppercase {
		const offset = 27 - 'A'
		return int(c + offset)
	}

	panic("rune out of range")
}
