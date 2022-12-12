namespace Day10;

public class CpuCycleEventArgs : EventArgs
{
	public int X { get; set; }

	public CpuCycleEventArgs(int x) : base()
	{
		X = x;
	}
}
