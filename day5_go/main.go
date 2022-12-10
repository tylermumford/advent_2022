package main

import (
	"fmt"
)

func main() {
	loadInputs()

	fmt.Println("Sample has", len(inputs.sample.commands), "commands, and main input has", len(inputs.real.commands))
	fmt.Println("Sample has", len(inputs.sample.ship), "stacks, and main input has", len(inputs.real.ship))

	fmt.Println("Sample input:")
	inputs.sample.evaluate()
	fmt.Println(inputs.sample.ship)
	fmt.Println("Top crates after evaluation:", inputs.sample.ship.topCrates())

	fmt.Println()

	fmt.Println("Main input:")
	inputs.real.evaluate()
	fmt.Println(inputs.real.ship)
	fmt.Println("Top crates after evaluation:", inputs.real.ship.topCrates())
}
