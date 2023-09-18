INT = lambda: int(input())
STR = lambda: str(input())
MI = lambda: map(int, input().split())
MI_DEC = lambda: map(lambda x: int(x) - 1, input().split()) 
LI = lambda: list(map(int, input().split()))

#----------------------------------
import itertools

N, K = map(int, input().split())
T = [LI() for _ in range(N)]
answer = 0

for route in itertools.permutations(range(N)):

    if route[0] != 0:
      continue
  
    time = 0
    for i in range(N-1):
      time += T[route[i]][route[i+1]]

    time += T[route[N-1]][route[0]]

    if time == K:
      answer += 1

print(answer)




