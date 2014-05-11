def P015():
  grid_size = 20
  grid_size_float = float(grid_size)
  result = 1

  for i in xrange(1, grid_size + 1):
    result *= (2 * grid_size_float + 1 - i) / i

  return int(result)

print P015()