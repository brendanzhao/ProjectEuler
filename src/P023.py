def divisors(num):
  divisors = [1, num]
  sqrt = int(num ** 0.5)

  if num == sqrt * sqrt:
    divisors.append(sqrt)
    sqrt -= 1

  for i in xrange(2, sqrt + 1):
    if not num % i:
      divisors += [i, (num / i)]

  return divisors

def P023():
  limit = 28123
  abundant = []
  non_abundant_sum = set(xrange(limit + 1))

  for i in xrange(2, limit + 1):
    if sum(divisors(i)) - i > i:
      abundant.append(i)
      for j in abundant:
        single_sum = i + j
        if single_sum < limit + 1 and single_sum in non_abundant_sum:
          non_abundant_sum.remove(single_sum)

  return sum(non_abundant_sum)

print P023()
