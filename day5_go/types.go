package main

type stackId int

// stack is a slice of crates, in order from bottom to top
type stack []crate

type crate rune

type command struct {
	// n is how many crates to move
	n int

	from, to stackId
}

type commands []command

type ship map[stackId]stack
