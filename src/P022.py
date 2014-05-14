def get_score(name):
  return sum((ord(letter) - 64) for letter in name)

def P022():
  names = sorted(eval(open("txt/P022.txt").read()))
  return sum(get_score(name) * (i + 1) for i, name in enumerate(names))

print P022()