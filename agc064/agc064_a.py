N = int(input())
A = construct_sequence(N)

def construct_sequence(N):
  L = (N * (N - 1)) // 2 # 列の長さを計算

A = [0] * L # 初期化
idx = 0

for i in range(1, N + 1):
  for j in range(i):
    if j == 0:
      A[idx] = i
    elif j == i - 1:
      A[idx] = i - 1
    else:
      A[idx] = i - 2
      idx += 1

    
print(A)
