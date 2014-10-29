from math import sqrt

def is_pentagonal(number):
  pent_sum = (sqrt(1 + 24 * number) + 1) / 6
  return pent_sum == int(pent_sum);

def P045():
  i = 143

  while True:
    i += 1
    hexa_sum = i * (2 * i - 1);
    if is_pentagonal(hexa_sum):
      return hexa_sum

print P045()
