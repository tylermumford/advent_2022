package main

// A domain represents complete input data to the advent of code solution.
type domain struct {
	ship     ship
	commands commands
}

// Performs the commands on the ship.
func (d domain) evaluate() {
	d.ship.performCommands(d.commands)
}
