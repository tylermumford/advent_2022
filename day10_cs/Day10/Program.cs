using Day10;

// See https://aka.ms/new-console-template for more information
Console.WriteLine("Advent of Code, Day 10");

Console.WriteLine("Part 1:");
Console.WriteLine($"Sum of indicated signal strengths: {answerPart1()}");

int answerPart1()
{
	var input = Inputs.Main.ParseIntoInstructions();
	var cpu = new Cpu();
	var history = cpu.Execute(input);

	var keySteps = new List<int>
	{
		20, 60, 100, 140, 180, 220,
	};

	return keySteps
		.Select(step => history.SignalStrengthDuringStep(step))
		.Sum();
}