import math

def truncate_pi(N):
 pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
 truncated_pi = pi[:N+1]
 return truncated_pi

N = int(input())
result = truncate_pi(N+1)
print(result)
