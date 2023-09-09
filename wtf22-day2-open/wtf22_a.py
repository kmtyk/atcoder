def determine_hat_colors(S):
N = len(S)
red_count = 0
blue_count = 0
result = []

for i in range(N):
if S[i] == 'R':
red_count += 1
else:
blue_count += 1

for i in range(N):
if red_count > blue_count:
result.append('Yes' if S[i] == 'R' else 'No')
elif red_count < blue_count:
result.append('Yes' if S[i] == 'B' else 'No')
else:
result.append('No')

return result

T = int(input())

results = []

for _ in range(T):
S = input() 
result = determine_hat_colors(S)
results.append(result)

for result in results:
print(' '.join(result))
