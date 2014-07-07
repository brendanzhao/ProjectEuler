import math

def sieve(limit):
  primes_set = set()
  primes = [True] * limit
  primes[0] = primes[1] = False

  for (i, is_prime) in enumerate(primes):
    if is_prime:
      primes_set.add(i)
      for n in xrange(i*i, limit, i):
        primes[n] = False

  return primes_set

def P035():
  limit = 1000000
  prime_set = sieve(limit)
  count = 0

  for prime in prime_set:
    rotating_prime = prime
    rotation_count = int(math.log10(prime))

    for _ in xrange(rotation_count):
      rotating_prime, digit = divmod(rotating_prime, 10)
      rotating_prime += digit * 10 ** (rotation_count)

      if rotating_prime not in prime_set:
        count += 1
        break

  return len(prime_set) - count

print P035()