using System.Text;

namespace Day10;

/// <summary>
/// The record of states a CPU was in while it executed instructions.
/// Contains things like register values and current step numbers.
/// </summary>
public class StateHistory
{
    private record struct HistoryEntry(int Cycle, int X) {};

    private List<HistoryEntry> History = new();

    public void Push(int x)
    {
        var cycle = History.Count + 1;
        History.Add(new HistoryEntry(cycle, x));
    }

    public int XValueAfterStep(int step)
    {
        return History.Single(h => h.Cycle == step).X;
    }

    /// <summary>
    /// Signal strength is the X value times the cycle number. 
    /// Cycle numbers are 1-based.
    /// </summary>
    public int SignalStrengthDuringStep(int step)
    {
        if (step == 1)
        {
            return 1;
        }

        var prev = History.Single(h => h.Cycle == step - 1);

        return prev.X * step;
    }

    public int CycleCount => History.Count;

    public string Visualize()
    {
        var sb = new StringBuilder();

        foreach (var h in History)
        {
            sb.Append($"After {h.Cycle}: X={h.X}\n");
        }

        return sb.ToString();
    }
}
