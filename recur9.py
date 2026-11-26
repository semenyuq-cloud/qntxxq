def NOD(A, B):
  if B == 0:
    return A
  return NOD(B, A % B)
A = int(input())
B = int(input())
C = int(input())
D = int(input())
print(NOD(A, B))
print(NOD(A, C))
print(NOD(A, D))
