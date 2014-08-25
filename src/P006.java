public class P006
{
	public static void main(String[] args)
	{
		run();
	}

	public static void run()
	{
		int squareOfSums = (int) Math.pow(EulerUtility.arithmeticSeries(100, 1, 100), 2);
		int sumOfSquares = EulerUtility.sumOfSquares(100);


		System.out.println(String.format("%d", squareOfSums - sumOfSquares));
	}
}
