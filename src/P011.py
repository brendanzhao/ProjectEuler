def prod(iterable):
  p = 1
  for n in iterable:
    p *= n
  return p


matrix = [[int(element) for element in line.split()]
    for line in open('P011.txt', 'r')]

length = 20
m = -1

for i in xrange(length):
  for j in xrange(length):
    # -
    if j < 17:
      m = max(m, prod(matrix[i][j + k] for k in xrange(4)))
      # /
      if i > 2:
        m = max(m, prod(matrix[i - k][j + k] for k in xrange(4)))
    # |
    if i < 17:
      m = max(m, prod(matrix[i + k][j] for k in xrange(4)))
      # \
      if j < 17:
        m = max(m, prod(matrix[i + k][j + k] for k in xrange(4)))

print m