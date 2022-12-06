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

	fmt.Println()

	fmt.Println("Main input:")
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
