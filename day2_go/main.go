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

	part1TotalScore := 0
	part2TotalScore := 0

	for _, line := range lines {
		if line == "" {
			continue
		}

		match := convertLineToMatch(line)

		part1TotalScore += match.scorePart1()
		part2TotalScore += match.scorePart2()
	}

	fmt.Println("Total score, part 1:", part1TotalScore)
	fmt.Println("Total score, part 2:", part2TotalScore)
}

const rock = "rock"
const paper = "paper"
const scissors = "scissors"

type move string

type match struct {
	// opponent is the move our opponent plays
	opponent move

	// player is the move we should play, assumed in part 1
	player move

	// goal is the outcome we need according to part 2
	goal outcome

	// realMove is the move we need to play to get the outcome according to part 2
	realMove move
}

type lookup map[move]map[move]int

// outcomes is indexed by [opponent move] and then [player move]
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

func (match match) scorePart1() int {
	return outcomes[match.opponent][match.player]
}

func (match match) scorePart2() int {
	return outcomes[match.opponent][match.realMove]
}

var moveEncoding = map[string]move{
	"A": rock,
	"B": paper,
	"C": scissors,
	"X": rock,
	"Y": paper,
	"Z": scissors,
}

var outcomeEncoding = map[string]outcome{
	"X": lose,
	"Y": draw,
	"Z": win,
}

const win = "win"
const draw = "draw"
const lose = "lose"

type outcome string

func convertLineToMatch(line string) match {
	symbols := strings.Split(line, " ")
	if len(symbols) != 2 {
		panic("A line didn't have 2 symbols: " + line)
	}

	opponent := moveEncoding[symbols[0]]
	goal := outcomeEncoding[symbols[1]]

	return match{
		opponent: opponent,
		player:   moveEncoding[symbols[1]],

		goal:     goal,
		realMove: deducePlayerMove(goal, opponent),
	}
}

// Example:
// howToReachOutcome[rock][win] = paper
var howToReachOutcome = map[move]map[outcome]move{
	rock:     {win: paper, lose: scissors, draw: rock},
	paper:    {win: scissors, lose: rock, draw: paper},
	scissors: {win: rock, lose: paper, draw: scissors},
}

func deducePlayerMove(goal outcome, opponent move) move {
	return howToReachOutcome[opponent][goal]
}
