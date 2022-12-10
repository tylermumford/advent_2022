namespace Day10;

/// <summary>
/// An instruction that adds v to the current value of x, at the end of two cycles.
/// </summary>
public record struct Addx(int v) : IInstruction
{

}
