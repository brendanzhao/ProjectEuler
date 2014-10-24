def P040():
  numbers = [0]
  product = 1
  digit = 1

  for i in xrange(1, 200000):
    for j in str(i):
      numbers.append(j)

  for i in xrange(7):
    product *= int(numbers[digit])
    digit *= 10

  return product

print P040()