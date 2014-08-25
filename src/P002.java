public class P002
{
	public static void main(String[] args)
	{
		run();
	}

	public static void run()
	{
		int previous = 1;
		int current = 2;
		int fibonacciSum;
		int sum = 0;

		while (current < 4000000)
		{
			if (current % 2 == 0)
			{
				sum += current;
			}

			fibonacciSum = previous + current;
			previous = current;
			current = fibonacciSum;
		}

		System.out.println(String.format("%d", sum));
	}
}
