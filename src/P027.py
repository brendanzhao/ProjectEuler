def sieve(limit):
  primes = [True] * limit
  primes[0] = primes[1] = False

  for (i, is_prime) in enumerate(primes):
    if is_prime:
      yield i
      for n in xrange(i*i, limit, i):
        primes[n] = False

def P027():
  primes = set(i for i in sieve(4000000))
  a = b = c = 0
  max_num_primes = -1
  result = -1

  for a in xrange(-999, 1000, 2):
    for b in sieve(1000):
      n = 0
      while (n ** 2 + a * n + b) in primes:
        n += 1

      if n > max_num_primes:
        max_num_primes = n
        result = a * b

  return result

print P027()