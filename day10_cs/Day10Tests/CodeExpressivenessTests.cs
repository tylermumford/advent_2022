namespace Day10Tests;

public class CodeExpressivenessTests
{
    [Fact]
    public void ThereIsACpu()
    {
        _ = new Cpu();
    }

    [Fact]
    public void ThereAreInstructions()
    {
        IInstruction _ = new Noop();
    }

    [Fact]
    public void CpuCanRunInstructions()
    {
        var cpu = new Cpu();

        var program = new List<IInstruction>
        {
            new Noop(),
            new Noop(),
            new Noop(),
        };

        cpu.Execute(program);
    }

    [Fact]
    public void TwoTypesOfInstructions()
    {
        var noOp = new Noop();

        var add = new Addx(-3);

        _ = new List<IInstruction>
        {
            noOp,
            add,
        };
    }

    [Fact]
    public void ExecutionProducesStateHistory()
    {
        var cpu = new Cpu();

        var program = new List<IInstruction>();

        StateHistory stateHistory = cpu.Execute(program);
    }

    [Fact]
    public void StateHistoryCanBeQueried()
    {
        var cpu = new Cpu();
        var history = cpu.Execute(new List<IInstruction>());

        try
        {
            history.SignalStrengthDuringStep(20);
        }
        catch {}
    }
}
