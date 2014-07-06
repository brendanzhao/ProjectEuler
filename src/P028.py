def corners(n):
  if n == 0:
    return 1

  return 4 * (2 * n + 1) ** 2 - 12 * n + corners(n - 1)

def P028():
  return corners(500)

print P028()