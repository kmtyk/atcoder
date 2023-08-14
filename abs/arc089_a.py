from sys import stdin

n = int(stdin.readline())
for i in range(n):
    t, x, y = map(int, stdin.readline().split())
    dist = x + y
    if t < dist or (dist % 2) != (t % 2):
        print("No")
        exit()

print("Yes")
