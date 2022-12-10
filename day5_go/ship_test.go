package main

import (
	"fmt"
	"reflect"
	"testing"
)

var sampleShip = `
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3
`

func Exampleship_String() {
	s := NewShipWithStacks([]stack{
		{"Z", "N"},
		{"M", "C", "D"},
		{"P"},
	})
	fmt.Println(s)
	//Output:
	//1: Z,N
	//2: M,C,D
	//3: P
}

func Exampleship_String_superSimple() {
	s := NewShipWithStacks([]stack{
		{"A", "B"},
	})
	fmt.Println(s)
	//Output:
	//1: A,B
}

func TestParseShip(t *testing.T) {
	expected := NewShipWithStacks([]stack{
		{"Z", "N"},
		{"M", "C", "D"},
		{"P"},
	})

	got := parseShip(sampleShip)

	isEqual := reflect.DeepEqual(got, expected)

	if !isEqual {
		t.Errorf("Result does not equal expectations.\nExpected:\n%v\nGot:\n%v",
			expected,
			got)
	}
}

func TestInferIndexes(t *testing.T) {
	input := " 1   2   3   4   5   6   7   8   9"
	expect := []int{1, 5, 9, 13, 17, 21, 25, 29, 33}

	got := inferIndexes(input)

	if !reflect.DeepEqual(expect, got) {
		t.Errorf("Expected %v but got %v", expect, got)
	}
}

func TestParseCommand(t *testing.T) {
	cases := []string{
		"move 1 from 2 to 1",
		"move 28 from 0 to 80",
	}

	expectations := []command{
		{n: 1, from: 2, to: 1},
		{n: 28, from: 0, to: 80},
	}

	for i := range cases {
		_case := cases[i]
		expect := expectations[i]

		result := parseCommand(_case)

		if expect != result {
			t.Errorf("%v: expected %v, got %v", _case, expect, result)
		}
	}
}

func TestTopCrates(t *testing.T) {
	s := parseShip(sampleShip)

	top := s.topCrates()

	if top != "NDP" {
		t.Errorf("Expected %v but got %v", "NDP", top)
	}
}

func TestPerformCommand(t *testing.T) {
	s := parseShip(sampleShip)
	c := command{
		n:    2,
		from: 2,
		to:   3,
	}
	expect := NewShipWithStacks([]stack{
		{"Z", "N"},
		{"M"},
		{"P", "D", "C"},
	})

	s.performCommand(c)

	if !reflect.DeepEqual(s, expect) {
		t.Errorf("performCommand failed, expected\n%v\nbut got\n%v", expect, s)
	}
}
