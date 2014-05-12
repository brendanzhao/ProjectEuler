def P018():
  triangle = [[int(value) for value in line.split()]
      for line in open('txt/P067.txt')]
  length = len(triangle)

  for i in xrange(length - 2, -1, -1):
    for j in xrange(i + 1):
      triangle[i][j] = max(triangle[i + 1][j], triangle[i + 1][j + 1]) + triangle[i][j]

  return triangle[0][0]

print P018()