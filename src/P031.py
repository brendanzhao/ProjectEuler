def P031():
  limit = 200
  coins = [1, 2, 5, 10, 20, 50, 100, 200]
  number_ways = [0] * (limit + 1)
  number_ways[0] = 1

  for i in coins:
    for j in xrange(i, len(number_ways)):
      number_ways[j] += number_ways[j - i]

  return number_ways[200]

print P031()