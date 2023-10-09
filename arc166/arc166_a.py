T = int(input())

def match_strings(T, test_cases):
results = []
for test_case in test_cases:
 X, Y = test_case
 count_A = X.count('A')
 count_B = X.count('B')
 count_AB = X.count('AB')

# 操作によってAの数とBの数を増やすことができる
# 操作によってABの数を増やすことができる
# ただし、ABの数を増やす操作がある場合、AとBの数は1つずつ増える
# なので、Xに含まれるAとBの数の合計がYに含まれるAとBの数の合計以上であれば一致させることができる
if count_A + count_B >= Y.count('A') + Y.count('B') and count_AB >= Y.count('AB'):
 results.append("YES")
else:
 results.append("NO")
 
return results
