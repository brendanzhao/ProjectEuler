def P039():
  max_solution_count = 0
  solution_count = 0
  result = 0

  for p in xrange(2, 1002, 2):
    solution_count = 0
    for a in xrange(2, p / 3):
      if (p * (p - 2 * a)) % (2 * (p - a)) == 0:
        solution_count += 1
    if solution_count > max_solution_count:
      max_solution_count = solution_count
      result = p

  return result

print P039()
