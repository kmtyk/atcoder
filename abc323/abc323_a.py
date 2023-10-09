S = input()

for i in range(2, 17, 2):
  if S[i-1] != '0': 
   print("No")
   break
 
if i == 16:
  print("Yes")
