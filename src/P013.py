from math import log10

def P013():
  total = sum(int(line) for line in open('txt/P013.txt'))
  digits = int(log10(total ) + 1)
  return total // (10 ** (digits - 10))

print P013()