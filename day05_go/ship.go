package main

import (
	"fmt"
	"strings"
)

// A ship is a slice of stacks of crates.
type ship struct {
	stacks           []stack
	isCrateMover9001 bool
}

// Returns a new ship. The size parameter is how
// many stacks are on the ship.
func NewShip(size int) ship {
	return ship{
		stacks:           make([]stack, size),
		isCrateMover9001: false,
	}
}

// Helps to create customized ships in code.
func NewShipWithStacks(stacks []stack) ship {
	s := NewShip(0)
	s.stacks = stacks
	return s
}

func (s ship) stackCount() int {
	return len(s.stacks)
}

func (s *ship) setIsCrateMover9001(value bool) {
	s.isCrateMover9001 = value
}

func (s ship) String() string {
	b := strings.Builder{}

	for i, stack := range s.stacks {
		joined := strings.Join(stack, ",")
		fmt.Fprintf(&b, "%d: %v", i+1, joined)

		if i < len(s.stacks)-1 {
			b.WriteString("\n")
		}
	}

	if len(s.stacks) == 0 {
		b.WriteString("(empty ship)")
	}

	return b.String()
}

func (s ship) AddCrate(c crate, i stackId) {
	s.stacks[i] = append(s.stacks[i], c)
}

func (s ship) topCrates() string {
	result := ""
	for _, stack := range s.stacks {
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
	if s.isCrateMover9001 {
		s.moveAllCrates(c)
		return
	}

	for i := 0; i < c.n; i++ {
		s.moveSingleCrate(c)
	}
}

// Ignores the n parameter and just moves the top crate
// from one stack to another.
func (s ship) moveSingleCrate(c command) {
	fromStack := s.stacks[c.from-1]
	toStack := s.stacks[c.to-1]

	crate := fromStack[len(fromStack)-1]

	s.stacks[c.from-1] = fromStack[0 : len(fromStack)-1]
	s.stacks[c.to-1] = append(toStack, crate)
}

func (s ship) moveAllCrates(c command) {
	fromStack := s.stacks[c.from-1]
	toStack := s.stacks[c.to-1]

	stackLen := len(fromStack)
	start := stackLen - c.n
	crates := fromStack[start:stackLen]

	s.stacks[c.from-1] = fromStack[0:start]
	s.stacks[c.to-1] = toStack.append(crates)
}
