def P036():
  limit = 1000000
  result = 0

  for i in xrange(1, limit, 2):
    if is_palindrome_integer(i, 2) and is_palindrome_integer(i, 10):
      result += i

  return result

def is_palindrome_integer(number, base):
  reverse = 0
  k = number

  while k > 0:
    reverse = base * reverse + k % base
    k /= base

  return reverse == number

print P036()