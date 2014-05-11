def P009():
  total = 1000
  a_limit = total / 3
  b_limit = total / 2

  for a in xrange(a_limit):
    for b in xrange(b_limit):
      c = total - a - b

      if (a * a + b * b == c * c):
        return a * b * c

print P009()