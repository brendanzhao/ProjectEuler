def fibonacci():
  a, b = 0, 1

  while True:
    yield a
    a, b = b, a + b

def P025():
  count = 0
  for x in fibonacci():
    if len(map(int, str(x))) == 1000:
      return count

    count += 1

print P025()
