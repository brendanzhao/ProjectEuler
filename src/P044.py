from math import sqrt

def is_pentagonal(number):
  pent_sum = (sqrt(1 + 24 * number) + 1) / 6
  return pent_sum == int(pent_sum);

def P044():
  found = False
  i = 1
  difference = -1

  while not found:
    i += 1
    pent_one = i * (3 * i - 1) / 2

    for j in xrange(i - 1, 0, -1):
      pent_two = j * (3 * j - 1) / 2
      if is_pentagonal(pent_one - pent_two) and is_pentagonal(pent_one + pent_two):
        difference = pent_one - pent_two
        found = True
        break

  return difference

print P044()