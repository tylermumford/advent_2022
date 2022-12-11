namespace Day10;

/// <summary>
/// Represents a CPU in the story. Has a register and performs instructions.
/// </summary>
public class Cpu
{
    // X starts at 1, as defined by the day's story.
    private int registerX = 1;

    public StateHistory Execute(IEnumerable<IInstruction> program)
    {
        var history = new StateHistory();

        foreach (var op in program)
        {
            if (op is Noop)
            {
                history.Push(x: registerX);
                continue;
            }
            else if (op is Addx add)
            {
                history.Push(x: registerX);
                registerX += add.v;
                history.Push(x: registerX);
                continue;
            }
        }

        return history;
    }
}
