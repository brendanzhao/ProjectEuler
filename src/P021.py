def divisors(num):
  divisors = [1, num]
  sqrt = int(num ** 0.5)

  if num == sqrt * sqrt:
    divisors.append(sqrt)
    sqrt -= 1;

  for i in xrange(2, sqrt):
    if not num % i:
      divisors += [i, (num / i)]

  return divisors

def P021():
  limit = 10000
  amicable_sum = 0

  for i in xrange(2, limit + 1):
    factors_i = sum(divisors(i)) - i
    if factors_i > i and factors_i <= limit:
      factors_j = sum(divisors(factors_i)) - factors_i
      if factors_j == i:
        amicable_sum += i + factors_i

  return amicable_sum

print P021()