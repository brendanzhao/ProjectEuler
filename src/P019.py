def P019():
  days = 2
  count = 0

  for i in xrange(1901, 2001):
    for j in xrange(1, 13):
      days_in_month = get_days_in_month(j, i)
      days += days_in_month
      days %= 7

      if days == 0:
        count += 1

  return count

def get_days_in_month(month, year):
  if month == 2:
    return 29 if year % 4 == 0 and year % 100 or year % 400 == 0 else 28
  elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    return 31
  else:
    return 30

print P019()