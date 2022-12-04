package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	file, err := os.ReadFile("sampleInput")
	if err != nil {
		panic(err)
	}

	input := string(file)
	lines := strings.Split(input, "\n")

	fmt.Println("Loaded", len(lines), "lines of input")
}
