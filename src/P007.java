import java.util.ArrayList;
import java.util.List;

public class P007
{
	public static void main(String[] args)
	{
		run();
	}

	public static void run()
	{
		int index;
		int current = 1;
		boolean currentIsPrime;
		List<Integer> primes = new ArrayList<Integer>();
		primes.add(2);

		while (primes.size() < 10001)
		{
			current += 2;
			index = 0;
			currentIsPrime = true;

			while (primes.get(index) * primes.get(index) <= current)
			{
				if (current % primes.get(index++) == 0)
				{
					currentIsPrime = false;
					break;
				}
			}

			if (currentIsPrime)
			{
				primes.add(current);
			}
		}

		System.out.println(String.format("%d", current));
	}
}