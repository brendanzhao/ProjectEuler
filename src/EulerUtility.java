public class EulerUtility
{
	private EulerUtility()
	{
		throw new UnsupportedOperationException("This should never be instantiated.");
	}
	
	public static boolean isPalindrome(int number)
	{
		String palindrome = Integer.toString(number);
		
		for (int i = 0, j = palindrome.length() - 1; i < palindrome.length() / 2; i++, j--)
		{
			if (palindrome.charAt(i) != palindrome.charAt(j))
			{
				return false;
			}
		}
		
		return true;
	}
	
	public static int gcd(int largerNumber, int smallerNumber) 
	{
        return (smallerNumber == 0) ? largerNumber : gcd(smallerNumber, largerNumber % smallerNumber);
	}
	
	public static int lcm(int numberOne, int numberTwo)
	{
		return numberOne % numberTwo == 0 ? numberOne : numberOne * numberTwo / gcd(numberOne, numberTwo);
	}
	
	public static int arithmeticSeries(int numberOfTerms, int firstTerm, int lastTerm)
	{
		return (int)((double)numberOfTerms / 2  * (firstTerm + lastTerm));
	}
	
	public static int sumOfSquares(int numberOfTerms)
	{
		return (int)(((double)numberOfTerms / 6) * (numberOfTerms + 1) * (2 * numberOfTerms + 1));
	}
}
