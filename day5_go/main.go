package main

import (
	"fmt"
)

func main() {
	loadInputs()

	fmt.Println("Sample has", len(inputs.sample.commands), "commands, and main input has", len(inputs.real.commands))
	fmt.Println("Sample has", len(inputs.sample.ship), "stacks, and main input has", len(inputs.real.ship))

	fmt.Println("Sample input:")

	fmt.Println()

	fmt.Println("Main input:")
}
