def P014():
  number = 1000000
  cache = [1] * (number + 1)
  largest = {'start_num': 1, 'distance': 1}

  for i in xrange(2, number + 1):
    distance = 0
    n = i

    while n != 1 and n >= i:
      distance += 1
      n = 3 * n + 1 if n % 2 else n / 2

    cache[i] = cache[n] + distance
    largest = {'start_num': i, 'distance': cache[i]} if cache[i] > largest['distance'] else largest

  return largest['start_num']

print P014()