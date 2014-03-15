import org.junit.Test;

public class P006
{
	
	@Test
	public void run()
	{
		int squareOfSums = (int) Math.pow(EulerUtility.arithmeticSeries(100, 1, 100), 2);
		int sumOfSquares = EulerUtility.sumOfSquares(100);
		
		// 25164150
		System.out.println(String.format("Problem 6: %d", squareOfSums - sumOfSquares));
	}
}
