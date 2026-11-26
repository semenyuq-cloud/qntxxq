def RootK(x, k, n):
  if n == 0:
    return 1
  y = RootK(x, k, n - 1)
  return y - (y - x / (y ** (k - 1))) / k


x = float(input())
k = int(input())

for i in range(6):
  n = int(input())
  print(RootK(x, k, n))
