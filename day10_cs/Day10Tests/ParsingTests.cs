namespace Day10Tests;

public class ParsingTests
{
    [Fact]
    public void ParseSmallInput()
    {
        var input = Inputs.Small;

        var program = input.ParseIntoInstructions();

        Assert.Equal(3, program.Count());
        Assert.Equal(new Noop(), program.ElementAt(0));

        Assert.IsType<Addx>(program.ElementAt(1));

        var secondElement = (Addx)program.ElementAt(1);
        Assert.Equal(3, secondElement.v);

        var thirdElement = (Addx)program.ElementAt(2);
        Assert.Equal(-5, thirdElement.v);
    }

    [Fact]
    public void ParseLargerInput()
    {
        var input = Inputs.Larger;

        var program = input.ParseIntoInstructions();

        Assert.Equal(146, program.Count());
        Assert.Equal(-36, ((Addx)program.ElementAt(44)).v);
    }
}
