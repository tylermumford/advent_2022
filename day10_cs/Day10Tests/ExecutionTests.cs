using Xunit.Abstractions;

namespace Day10Tests;

public class ExecutionTests
{
    private ITestOutputHelper Output;
    
    public ExecutionTests(ITestOutputHelper output)
    {
        Output = output;
    }

    [Fact]
    public void SuperSimpleInput()
    {
        var c = new Cpu();
        var program = Inputs.Small.ParseIntoInstructions();

        var result = c.Execute(program);

        // Just to save some keystrokes
        var xval = (int step) => result.XValueAfterStep(step);

        try
        {
            Assert.Equal(5, result.CycleCount);
            Assert.Equal(1, xval(1));
            Assert.Equal(1, xval(2));
            Assert.Equal(4, xval(3));
            Assert.Equal(4, xval(4));
            Assert.Equal(-1, xval(5));
        }
        catch
        {
            Output.WriteLine("StateHistory (result):");
            Output.WriteLine(result.Visualize());
            throw;
        }
    }

    [Fact]
    public void LargerInput()
    {
        var c = new Cpu();
        var program = Inputs.Larger.ParseIntoInstructions();

        var result = c.Execute(program);

        // Just to save some keystrokes
        var xAssert = (int step, int expect) =>
        {
            var x = result.XValueAfterStep(step);
            Assert.Equal(expect, x);
        };

        var sigAssert = (int step, int expect) =>
        {
            var signal = result.SignalStrengthDuringStep(step);
            Assert.Equal(expect, signal);
        };

        try
        {
            Assert.True(result.CycleCount >= 220);

            // These cases are based on the story for day 10.
            xAssert(19, 21);
            xAssert(59, 19);
            xAssert(99, 18);

            sigAssert(20, 420);
            sigAssert(60, 1140);
            sigAssert(220, 3960);
        }
        catch
        {
            Output.WriteLine("StateHistory (result):");
            Output.WriteLine(result.Visualize());
            throw;
        }
    }
}
