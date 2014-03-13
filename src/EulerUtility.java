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
}
