def P029():
  distinct = set()

  for i in xrange(2, 101):
    for j in xrange(2, 101):
        distinct.add(i ** j)

  return len(distinct)

print P029()