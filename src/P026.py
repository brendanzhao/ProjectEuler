def P026():
  repeat_length = 0
  d = -1

  for i in xrange(1000, 0, -1):
    if repeat_length >= i:
      break

    remainders = set()
    remainder = 1

    while remainder != 0 and remainder not in remainders:
      remainders.add(remainder)
      remainder *= 10
      remainder %= i


    new_length = len(remainders)
    if new_length > repeat_length:
      repeat_length, d = new_length, i

  return d

print P026()
