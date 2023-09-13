INT = lambda: int(input())
STR = lambda: str(input())
MI = lambda: map(int, input().split())
MI_DEC = lambda: map(lambda x: int(x) - 1, input().split()) 
LI = lambda: list(map(int, input().split()))

#----------------------------------
S = "abcdefghijklmnopqrstuvwxyz"
X = [0]*len(S)
M = STR()
for i in M:
  index = S.index(i)
  X[index] += 1

A = "Yes"
for j in X:
  if j % 2 != 0:
    A = "No"
    break

print(A)
    
