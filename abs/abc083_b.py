N,A,B=map(int,input().split())

c=0
for x in range(1,N+1):
  y=list(str(x))

  z=sum([int(a) for a in y])

  if A<=z and z<=B:
    c+=x

print(c)
