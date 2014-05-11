def get_triangular_num():
  n = 0

  while True:
    n += 1
    yield n * (n + 1) / 2

def get_num_divisors(num):
  num_divisors = 0
  sqrt_limit = int(num ** 0.5)

  for i in xrange(1, sqrt_limit):
    if num % i == 0:
      num_divisors += 2

  if sqrt_limit * sqrt_limit == num:
    num_divisors -= 1

  return num_divisors

for n in get_triangular_num():
  if get_num_divisors(n) > 500:
    print n
    break
