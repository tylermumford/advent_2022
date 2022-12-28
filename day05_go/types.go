package main

type stackId int

// stack is a slice of crates, in order from bottom to top
type stack []crate

// Returns a new stack.
// I thought this wouldn't be necessary, but
// it seems Go's type inference requires it.
func (st stack) append(crates []crate) stack {
	result := st

	for _, c := range crates {
		result = append(result, c)
	}

	return result
}

type crate = string

type commands []command

type command struct {
	// n is how many crates to move
	n int

	from, to stackId
}
