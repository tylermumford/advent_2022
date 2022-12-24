package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestPacketPairs(t *testing.T) {
	_ = packetPair{
		left:  packet{},
		right: packet{},
	}
}

func TestStringToPacket(t *testing.T) {
	cases := []string{
		"[9]",
		"[[1],[2,3,4]]",
	}
	expects := []packet{
		{9},
		{[]int{1}, []int{2, 3, 4}},
	}

	for i := range cases {
		p := newPacket(cases[i])

		assert.EqualValues(t, expects[i], p)
	}
}

func TestFixConcreteTypes(t *testing.T) {
	cases := []packet{
		{7.0},
		{-12.0, 14.8},
		{[]any{12.0}},
		{[]any{12.0}, 15.0},
		{[]any{[]any{5.0}}},
	}
	expects := []packet{
		{7},
		{-12, 14},
		{[]int{12}},
		{[]int{12}, 15},
		{[]any{[]int{5}}},
	}

	for i := range cases {
		fixConcreteTypes(cases[i])
		assert.Equal(t, expects[i], cases[i])
	}
}
