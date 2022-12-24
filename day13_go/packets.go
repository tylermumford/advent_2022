package main

import (
	"encoding/json"
)

// Types

// A slice whose items are either ints or slices of ints, or a combination of both.
type packet []any

type packetPair struct {
	left  packet
	right packet
}

// Functions and methods

func newPacket(in string) packet {
	result := packet{}

	err := json.Unmarshal([]byte(in), &result)
	if err != nil {
		panic(err)
	}

	fixConcreteTypes(result)
	return result
}

// Since json.Unmarshal uses float64 instead of int and []interface{} instead of []int,
// this function replaces those values with the needed types.
func fixConcreteTypes(p []any) {
	for i := range p {
		if value, ok := p[i].(float64); ok {
			p[i] = int(value)
		} else if nested, ok := p[i].([]any); ok {
			fixConcreteTypes(nested)

			if ints, ok := allInts(nested); ok {
				p[i] = ints
			}
		}
	}
}

func allInts(x []any) ([]int, bool) {
	result := make([]int, 0, len(x))
	for i := range x {
		if value, ok := x[i].(int); ok {
			result = append(result, value)
		} else {
			return nil, false
		}
	}
	return result, true
}
