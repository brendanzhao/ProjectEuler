from fractions import Fraction

def P033():
  # 10a + x / 10x + b = a / b
  num = 1
  den = 1

  for x in xrange(1, 10):
    for a in xrange(1, 10):
      for b in xrange(a + 1, 10):
        if float(10 * a + x) / float(10 * x + b) == float(a) / float(b):
          num *= a
          den *= b

  return Fraction(num, den).denominator

print P033()
