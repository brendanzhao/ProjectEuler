def is_pandigital(number, digits):
  if number != number[:digits]:
    return False

  for i in map(str, xrange(1, digits + 1)):
    if i not in number:
      return False
  return True

def P038():
  for i in xrange(9876, 9122, -1):
    if is_pandigital('%s%s' % (i, i * 2), 9):
      return '%s%s' % (i, i * 2)

print P038()
