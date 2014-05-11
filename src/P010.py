limit = 2000000
limit1 = limit + 1
sqrt_limit = int(2000000 ** 0.5)

all_numbers = range(limit1)
all_numbers[1] = 0

for i in xrange(3, sqrt_limit, 2):
  if all_numbers[i]:
    all_numbers[i * i: limit1: i] = [0] * len(all_numbers[i * i: limit1: i])

prime_sum = 2
for i in xrange(3, limit, 2):
  prime_sum += all_numbers[i]

print prime_sum
