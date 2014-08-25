public class P001
{
	public static void main(String[] args)
	{
		run();
	}

	public static void run()
	{
		int sum = 0;

		for (int i = 0; i < 1000; i++)
		{
			if (i % 3 == 0 || i % 5 == 0)
			{
				sum += i;
			}
		}

		System.out.println(String.format("%d", sum));
	}
}