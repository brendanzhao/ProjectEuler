public class P005
{
	public static void main(String[] args)
	{
		run();
	}

	public static void run()
	{
		int product = 2520;

		for (int i = 11; i < 21; i++)
		{
			product = EulerUtility.lcm(product, i);
		}

		System.out.println(String.format("%d", product));
	}
}
