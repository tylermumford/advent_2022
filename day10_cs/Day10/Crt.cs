using System.Text;

namespace Day10;

/// <summary>
/// A display that draws pixels based on the position of a sprite.
/// Closely tied to the Cpu clock mechanism.
/// </summary>
public class Crt
{
	const string LitPixel = "#";
	const string OffPixel = "-";

	private StringBuilder Buffer = new();
	private int NextPixel = 0;

	public void HandleSignal(object sender, CpuCycleEventArgs e)
	{
		Cycle(e.X);
	}

	/// <summary>Handles another cycle.</summary>
	public void Cycle(int spritePosition)
	{
		string next;

		var distance = Math.Abs(spritePosition - NextPixel);
		if (distance <= 1)
		{
			next = LitPixel;
		}
		else
		{
			next = OffPixel;
		}

		MaybeWrap();
		Buffer.Append(next);
		NextPixel++;
	}

	private void MaybeWrap()
	{
		// Remember that pixels are numbered
		// 0  .. 39
		// 40 .. 79
		if (NextPixel >= 40 && NextPixel % 40 == 0)
		{
			Buffer.Append("\n");
		}
	}

	/// <summary>Returns the display of the Crt, as text.</summary>
	public string Image()
	{
		return Buffer.ToString();
	}
}
