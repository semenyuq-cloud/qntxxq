def DigitSum(k):
  if k < 10:
    return k
  return  k % 10 + DigitSum(k // 10)
for i in range(5):
  k = int(input())
  print(DigitSum(k))
