import org.junit.Test;

public class P002
{
	@Test
	public void run()
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
		
		// 4613732
		System.out.println(String.format("Problem 2: %d", sum));
	}
}
