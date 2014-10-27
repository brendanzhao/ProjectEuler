def permute(number):
  if len(number) <= 1:
    yield number
  else:
    for permutation in permute(number[1:]):
      for i in xrange(len(number)):
        yield permutation[:i] + number[0] + permutation[i:]

def P043():
  primes = [2, 3, 5 ,7, 11, 13, 17]
  result = 0

  for number in permute('0123456789'):
    should_add = True

    for i in xrange(1, 8):
      if int(number[i] + number[i + 1] + number[i + 2]) % primes[i - 1]:
        should_add = False
        break

    if should_add:
      result += int(number)

  return result

print P043()
