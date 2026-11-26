def NOD(a, b):
  if b == 0:
    return a
  return NOD(b, a % b)

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(NOD(a, b))
print(NOD(a, c))
print(NOD(a, d))
