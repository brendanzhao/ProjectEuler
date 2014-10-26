from math import sqrt

def P042():
  words = eval(open('txt/P042.txt', 'r').read())
  result = 0

  for w in words:
    letter_sum = sum((ord(c) - 64) for c in w)
    triangular_sum = (sqrt(1 + 8 * letter_sum) - 1) / 2

    if triangular_sum == int(triangular_sum):
      result += 1

  return result

print P042()
