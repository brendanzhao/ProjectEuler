def P032():
  pandigitals = set()

  for i in xrange(1, 1000):
    for j in xrange(1, 2000):
      product = i * j
      if ''.join(sorted(str(i) + str(j) + str(product))) == '123456789':
        pandigitals.add(product)

  return sum(pandigitals)

print P032()
