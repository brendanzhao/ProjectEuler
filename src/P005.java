import org.junit.Test;

public class P005
{
	
	@Test
	public void test()
	{
		int product = 2520;
		
		for (int i = 11; i < 21; i++)
		{
			product = EulerUtility.lcm(product, i);
		}
		
		// 232792560
		System.out.println(String.format("Problem 5: %d", product));
	}	
}
