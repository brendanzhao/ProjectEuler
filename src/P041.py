from math import log10

def sieve(limit):
  primes = [True] * limit
  primes[0] = primes[1] = False

  for (i, is_prime) in enumerate(primes):
    if is_prime:
      yield i
      for n in xrange(i*i, limit, i):
        primes[n] = False

def is_pandigital(number):
  digits = int(log10(number)) + 1
  number_set = set(str(number))

  for i in map(str, xrange(1, digits + 1)):
    if i not in number_set:
      return False
  return True

def P041():
  limit = 7654321
  result = -1

  for prime in sieve(limit):
    if is_pandigital(prime):
      result = prime

  return result

print P041()
