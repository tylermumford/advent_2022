package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	initOutcomes()

	file, err := os.ReadFile("sampleInput")
	if err != nil {
		panic(err)
	}

	input := string(file)
	lines := strings.Split(input, "\n")

	fmt.Println("Loaded", len(lines), "lines of input")

	totalScore := 0

	for i, line := range lines {
		if line == "" {
			continue
		}

		match := convertLineToMatch(line)
		fmt.Printf("Round {%d}: %d points\n", i, match.score())

		totalScore += match.score()
	}

	fmt.Println("Total score:", totalScore)
}

const rock = "rock"
const paper = "paper"
const scissors = "scissors"

type move string

type match struct {
	opponent move
	player   move
}

type lookup map[move]map[move]int

var outcomes lookup

func initOutcomes() {
	outcomes = lookup{
		rock:     {rock: 4, paper: 8, scissors: 3},
		paper:    {rock: 1, paper: 5, scissors: 9},
		scissors: {rock: 7, paper: 2, scissors: 6},
	}
}

func printOutcomes() {
	// Used this function to inspect the outcomes table.

	i := 0
	for opponent, in := range outcomes {
		for player, score := range in {
			fmt.Println("(If they play", opponent, "and I play", player, "then I get", score, "points.)")
			i++
		}
	}
	fmt.Println("Outcomes table has", i, "outcomes")
}

func (match match) score() int {
	return outcomes[match.opponent][match.player]
}

var moveEncoding = map[string]move{
	"A": rock,
	"B": paper,
	"C": scissors,
	"X": rock,
	"Y": paper,
	"Z": scissors,
}

func convertLineToMatch(line string) match {
	moves := strings.Split(line, " ")
	if len(moves) != 2 {
		panic("A line didn't have 2 moves: " + line)
	}

	return match{
		opponent: moveEncoding[moves[0]],
		player:   moveEncoding[moves[1]],
	}
}
