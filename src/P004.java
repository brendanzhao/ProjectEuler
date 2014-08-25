public class P004
{
	public static void main(String[] args)
	{
		run();
	}

	public static void run()
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

		System.out.println(String.format("%d", maxPalindrome));
	}
}
