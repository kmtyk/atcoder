N = int(input())
a = list(map(int,input().split()))
a.sort()
a.reverse()
A = 0
B = 0
for i in range(N):
  if i % 2 == 0:
    A += a[i]
  else: 
    B += a[i]
print(A - B)
