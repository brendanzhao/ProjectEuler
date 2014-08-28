def is_pandigital(number, digits):
  if number != number[:digits]:
    return False

  for i in map(str, xrange(1, digits + 1)):
    if i not in number:
      return False
  return True

def P032():
  pandigitals = set()

  for i in xrange(1, 1000):
    for j in xrange(1, 2000):
      product = i * j
      if is_pandigital('%s%s%s' % (i, j, product), 9):
        pandigitals.add(product)

  return sum(pandigitals)

print P032()
