namespace Day10;

/// <summary>
/// String extension method(s) to parse CPU instructions.
/// </summary>
public static class ParsingExtensions
{
    public static IEnumerable<IInstruction> ParseIntoInstructions(this string input)
    {
        ArgumentNullException.ThrowIfNull(input);

        var lines = input.Split("\n");

        var result = new List<IInstruction>();
        foreach (var line in lines)
        {
            if (line == "noop")
            {
                result.Add(new Noop());
            }
            else if (line.StartsWith("addx"))
            {
                var v = ExtractArgument(line);
                result.Add(new Addx(v));
            }
            else
            {
                throw new NotImplementedException($"Input line {line} has unexpected instruction");
            }
        }

        return result;
    }

    private static int ExtractArgument(string instruction)
    {
        var argument = instruction.Replace("addx ", "");
        return int.Parse(argument);
    }
}
