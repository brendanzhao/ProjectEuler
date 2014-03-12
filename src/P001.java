import org.junit.Test;

public class P001
{
	@Test
	public void runProblem()
	{
		int sum = 0;
		
		for (int i = 0; i < 1000; i++)
		{
			if (i % 3 == 0 || i % 5 == 0)
			{
				sum += i;
			}
		}
		
		// 233168
		System.out.println(String.format("Problem 1: %d", sum));
	}
}