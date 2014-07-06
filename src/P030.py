def P030():
  limit = 9 ** 5 * 6
  total_result = 0

  for i in xrange(2, limit):
    number = i
    current_result = 0

    while (number > 0):
      digit = number % 10
      number /= 10
      current_result += digit ** 5

    if current_result == i:
      total_result += current_result

  return total_result

print P030()
