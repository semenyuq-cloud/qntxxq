def DigitSum(K):
  if K < 10:
    return K
  return K % 10 + DigitSum(K // 10)
for i in range(5):
  K = int(input())
  print(DigitSum(K))
