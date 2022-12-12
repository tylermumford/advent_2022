namespace Day10;

/// <summary>
/// A display that draws pixels based on the position of a sprite.
/// Closely tied to the Cpu clock mechanism.
/// </summary>
public class Crt
{
	public void HandleSignal(object sender, CpuCycleEventArgs e)
	{
		
	}

	/// <summary>Handles another cycle.</summary>
	public void Cycle(int spritePosition)
	{

	}

	/// <summary>Returns the display of the Crt, as text.</summary>
	public string Image()
	{
		return "";
	}
}
