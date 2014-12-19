def sieve(limit):
  primes = [True] * limit
  primes[0] = primes[1] = False

  for (i, is_prime) in enumerate(primes):
    if is_prime:
      yield i
      for n in xrange(i*i, limit, i):
        primes[n] = False

def P047():
  consecutive = 0
  primes = [_ for _ in sieve(50000)]
  i = 2 * 3 * 5 * 7

  while consecutive < 4:
    current = i
    prime_factor_count = 0

    for prime in primes:
      while not current % prime:
        current /= prime
        hit = True

      if hit:
        prime_factor_count += 1
        hit = False

      if current < prime:
        break

    if prime_factor_count == 4:
      consecutive += 1
    else:
      consecutive = 0
    i += 1

  return i - 4

print P047()