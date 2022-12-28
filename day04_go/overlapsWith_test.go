package main

import (
	"testing"
)

func TestOverlapsWith(t *testing.T) {
	data := []testCase{
		// Made up
		{"1-4", "4-10", true},
		{"1-1", "2-2", false},
		{"1-2", "2-2", true},
		// From sampleInput
		{"2-4", "6-8", false},
		{"2-3", "4-5", false},
		{"5-7", "7-9", true},
		{"2-8", "3-7", true},
		{"6-6", "4-6", true},
		{"2-6", "4-8", true},
	}

	for _, testCase := range data {
		sampleA := parseSpan(testCase.a)
		sampleB := parseSpan(testCase.b)

		testOverlapsWith(t, sampleA, sampleB, testCase.expect)
	}
}

type testCase struct {
	a, b   string
	expect bool
}

func testOverlapsWith(t *testing.T, sampleA, sampleB span, expect bool) {
	got1 := sampleA.overlapsWith(sampleB)
	got2 := sampleB.overlapsWith(sampleA)

	if got1 != expect {
		t.Errorf("%v overlaps with %v? Expected %v but got %v", sampleA, sampleB, expect, got1)
	}

	if got1 != got2 {
		t.Errorf("For %v and %v, overlapsWith should be symmetrical, but it isn't", sampleA, sampleB)
		t.Errorf("%v overlaps with %v: %v  --  %v overlaps with %v: %v",
			sampleA,
			sampleB,
			got1,
			sampleB,
			sampleA,
			got2)
	}
}
