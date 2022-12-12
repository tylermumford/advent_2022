namespace Day10Tests;

public class CrtTests
{
	const string Lit = "#";
	const string Off = "-";
	const int Width = 40;

	[Fact]
	public void CrtDrawsLitPixel()
	{
		var c = new Crt();

		c.Cycle(1);

		var result = c.Image();

		Assert.Equal(Lit, result);
	}

	[Fact]
	public void CrtDrawsOffPixel()
	{
		var c = new Crt();

		c.Cycle(100);

		var result = c.Image();

		Assert.Equal(Off, result);
	}

	[Fact]
	public void CpuCanMakeScreenDrawPixels()
	{
		var cpu = new Cpu();
		var screen = new Crt();
		cpu.DuringCycle += screen.HandleSignal;

		var program = "noop\nnoop\nnoop\nnoop".ParseIntoInstructions();
		cpu.Execute(program);

		var result = screen.Image();
		var expect = $"{Lit}{Lit}{Lit}{Off}";

		Assert.Equal(expect, result);
	}

	[Fact]
	public void AddXResultsInTwoPixels()
	{
		var cpu = new Cpu();
		var screen = new Crt();
		cpu.DuringCycle += screen.HandleSignal;

		var program = "addx 8".ParseIntoInstructions();
		cpu.Execute(program);

		var result = screen.Image();
		var expect = $"{Lit}{Lit}";

		Assert.Equal(expect, result);
	}

	[Fact]
	public void ImageWrapsAround()
	{
		var screen = new Crt();
		for (var i = 0; i < Width + 1; i++)
		{
			screen.Cycle(i);
		}

		var result = screen.Image();
		var expectLength = Width + 2;

		Assert.Contains("\n", result);
		Assert.Equal(expectLength, result.Length);
	}

	[Fact]
	public void ImageWrapsAtZeroIndex()
	{
		var screen = new Crt();
		for (var i = 0; i < Width + 1; i++)
		{
			screen.Cycle(1);
		}

		var result = screen.Image();
		var expectLength = Width + 2;

		Assert.Contains("\n", result);
		Assert.Equal(expectLength, result.Length);

		// The key to this test is that even though the screen.Cycle
		// method is always getting the value 1, it draws the pixel
		// on the second line as Lit, because the X register
		// only corresponds to horizontal position, not absolute position.
		var lastPixel = result.Substring(result.Length - 1, 1);
		Assert.Equal(Lit, lastPixel);
	}
}
