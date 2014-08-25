public class P003
{
	public static void main(String[] args)
	{
		run();
	}

	public static void run()
	{
		long number = 600851475143L;
		long divisor = 1L;

		while (divisor < number)
		{
			divisor += 2;

			while (number % divisor == 0)
			{
				number /= divisor;
			}
		}

		System.out.println(String.format("%d", divisor));
	}
}