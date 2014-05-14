from math import factorial

def P020():
  return sum(map(int, str(factorial(100))))

print P020()