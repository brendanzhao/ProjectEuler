def P009():
  sum = 1000
  a_limit = sum / 3
  b_limit = sum / 2

  for a in xrange(a_limit):
    for b in xrange(b_limit):
      c = sum - a - b

      if (a * a + b * b == c * c):
        return a * b * c

print P009()