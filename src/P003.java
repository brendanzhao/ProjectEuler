import org.junit.Test;

public class P003
{
	@Test
	public void run()
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
		
		// 6857
		System.out.println(String.format("Problem 2: %d", divisor));
	}
}