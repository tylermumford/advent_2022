package main

// A domain represents complete input data to the advent of code solution.
type domain struct {
	ship     ship
	commands commands
}

type stackId int

// stack is a slice of crates, in order from bottom to top
type stack []crate

type crate = string

type commands []command

type command struct {
	// n is how many crates to move
	n int

	from, to stackId
}
