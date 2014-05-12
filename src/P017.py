def convert_to_string(n):
  base_one = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
    'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
    'seventeen', 'eighteen', 'nineteen']
  base_two = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

  result = ''
  if n >= 1000:
    result += base_one [n // 1000] + 'thousand' + ('and' if n % 1000 else '')
    n %= 1000
  if n >= 100:
    result += base_one[n // 100] + 'hundred' + ('and' if n % 100 else '')
    n %= 100
  if n >= 20:
    result += base_two[n // 10]
    n %= 10
  if n > 0:
    result += base_one[n]

  return result

def P017():
  return sum(map(len, map(convert_to_string, xrange(1, 1001))))

print P017()