from math import log10

def sieve(limit):
  primes = []
  prime_bool_array = [True] * limit
  prime_bool_array[0] = prime_bool_array[1] = False

  for (i, is_prime) in enumerate(prime_bool_array):
    if is_prime:
      primes.append(i)
      for n in xrange(i*i, limit, i):
        prime_bool_array[n] = False

  return prime_bool_array, primes

def P037():
  prime_bool_array, primes = sieve(1000000)
  count = 0
  result = []
  k = 0

  for i in (2, 3, 5, 7):
    primes.remove(i)

  while count < 11:
    prime = primes[k]
    truncate_left = truncate_right = prime
    is_prime = True
    left_modulo = int(log10(prime) + 1) - 1

    while (truncate_right > 0 and is_prime):
      is_prime = prime_bool_array[truncate_left] and prime_bool_array[truncate_right]
      truncate_left %= 10**left_modulo
      truncate_right /= 10
      left_modulo -= 1

    if is_prime:
      count += 1
      result.append(prime)

    k += 1

  return sum(result)

print P037()
