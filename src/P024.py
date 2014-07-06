def factorial(n):
  if n == 0:
    return 0

  result = 1

  for i in xrange(1, n + 1):
    result *= i

  return result

def P024():
  numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  count = len(numbers)
  remainder = 1000000 - 1
  result = 0

  for i in xrange(1, count):
    current_factorial = factorial(count - i)
    quotient = remainder / current_factorial
    remainder %= current_factorial
    result += numbers.pop(quotient) * 10 ** (count - i)

  result += numbers.pop(0)
  return result

print P024()