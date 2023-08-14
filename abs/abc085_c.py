N,otoshi=map(int,input().split())
otoshi /= 1000
for a in range(N+1):
    for b in range(N+1):
        c = N - (a+b)
        if c<0:
            break
        if 10*a+5*b+c==otoshi:
            print("{} {} {}".format(a,b,c))
            exit()
print("-1 -1 -1")
