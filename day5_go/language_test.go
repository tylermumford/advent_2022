package main

import "testing"

func TestRuneToString(t *testing.T) {
	rune := 'S'

	if string(rune) != "S" {
		t.Errorf("Converted %v to string and got %v", rune, string(rune))
	}
}
