def RootK(X, K, N):
  if N == 0:
    return 1
  y = RootK(X, K, N - 1)
  return y - (y - X / (y ** (K - 1))) / K


X = float(input())
K = int(input())

for i in range(6):
  N = int(input())
  print(RootK(X, K, N))
