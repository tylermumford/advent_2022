package main

import (
	"fmt"
	"strings"
)

// A ship is a slice of stacks of crates.
type ship []stack

// Returns a new ship. The size parameter is how
// many stacks are on the ship.
func NewShip(size int) ship {
	return make(ship, size)
}

func (s ship) String() string {
	b := strings.Builder{}

	for i, stack := range s {
		joined := strings.Join(stack, ",")
		fmt.Fprintf(&b, "%d: %v", i+1, joined)

		if i < len(s)-1 {
			b.WriteString("\n")
		}
	}

	if len(s) == 0 {
		b.WriteString("(empty ship)")
	}

	return b.String()
}

func (s ship) AddCrate(c crate, i stackId) {
	s[i] = append(s[i], c)
}
