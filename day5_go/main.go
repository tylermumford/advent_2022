package main

import (
	"fmt"
)

func main() {
	loadInputs()

	fmt.Println("Sample has", len(inputs.sample.commands), "commands, and main input has", len(inputs.real.commands))
	fmt.Println("Sample has", inputs.sample.ship.stackCount(), "stacks, and main input has", inputs.real.ship.stackCount())

	fmt.Println()

	inputs.sample.evaluate()
	inputs.real.evaluate()

	fmt.Println("Sample input:")
	fmt.Println(inputs.sample.ship)
	fmt.Println("Top crates after evaluation:", inputs.sample.ship.topCrates())

	fmt.Println()

	fmt.Println("Sample input, part two!")
	fmt.Println(inputs.sample.ship9001)
	fmt.Println("Top crates after evaluation:", inputs.sample.ship9001.topCrates())

	fmt.Println()

	fmt.Println("Main input:")
	fmt.Println(inputs.real.ship)
	fmt.Println("Top crates after evaluation:", inputs.real.ship.topCrates())

	fmt.Println()

	fmt.Println("Main input, part two!")
	fmt.Println(inputs.real.ship9001)
	fmt.Println("Top crates after evaluation:", inputs.real.ship9001.topCrates())
}
