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

func (s ship) topCrates() string {
	result := ""
	for _, stack := range s {
		top := stack[len(stack)-1]
		result = result + top
	}
	return result
}

func (s ship) performCommands(commands []command) {
	for _, c := range commands {
		s.performCommand(c)
	}
}

func (s ship) performCommand(c command) {
	for i := 0; i < c.n; i++ {
		s.moveSingleCrate(c)
	}
}

// Ignores the n parameter and just moves the top crate
// from one stack to another.
func (s ship) moveSingleCrate(c command) {
	fromStack := s[c.from-1]
	toStack := s[c.to-1]

	crate := fromStack[len(fromStack)-1]

	s[c.from-1] = fromStack[0 : len(fromStack)-1]
	s[c.to-1] = append(toStack, crate)
}
