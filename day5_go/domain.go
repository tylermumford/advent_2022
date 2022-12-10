package main

// A domain represents complete input data to the advent of code solution.
type domain struct {
	ship     ship
	commands commands

	ship9001 ship
}

// Performs the commands on the ship(s).
func (d domain) evaluate() {
	d.ship.performCommands(d.commands)

	d.ship9001.performCommands(d.commands)
}
