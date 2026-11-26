a = [0] * 21
def Fib2(N):
  if N <= 2:
    return 1
  if a[N] == 0:
    a[N] = Fib2(N - 2) + Fib2(N - 1)
  return a[N]

for i in range(5):
  n = int(input())
  print(Fib2(n))
