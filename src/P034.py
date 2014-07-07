import time

def gen_factorial_cache(limit):
  cache = [1] * (limit + 1)

  for i in xrange(1, limit + 1):
    cache[i] = cache[i - 1] * i

  return cache

def get_digits(num):
  digits = []

  while num > 0:
    num, r = divmod(num, 10)
    digits.append(r)

  return digits

def P034():
  cache = gen_factorial_cache(9)
  limit = cache[9]
  result = 0

  for i in xrange(3, limit):
    digits = get_digits(i)
    total = sum([cache[j] for j in digits])
    if total == i:
      result += total

  return result

print P034()
