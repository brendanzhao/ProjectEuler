import org.junit.Test;

public class P004
{
	@Test
	public void test()
	{
		int maxPalindrome = -1;
		int palindrome = -1;
		
		for (int i = 100; i < 1000; i++)
		{
			for (int j = i; j < 1000; j++)
			{
				palindrome = i * j;
				
				if (palindrome > maxPalindrome && EulerUtility.isPalindrome(palindrome))
				{
					maxPalindrome = palindrome;
				}
			}
		}
		
		// 906609
		System.out.println(String.format("Problem 4: %d", maxPalindrome));
	}
}
