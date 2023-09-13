INT = lambda: int(input())
STR = lambda: str(input())
MI = lambda: map(int, input().split())
MI_DEC = lambda: map(lambda x: int(x) - 1, input().split()) 
LI = lambda: list(map(int, input().split()))

#----------------------------------
T = []
L,H = MI()
N = INT()
for i in range(N):
  A = INT()
  if A - L == 0 or A - H == 0:
    T.append(0)
    
  if A - L < 0:
    T.append(abs(A-L))
    
  if A - L > 0 and A - H < 0:
    T.append(0)
  
  if A - H > 0:
    T.append(-1)

for i in T:
  print(i)
