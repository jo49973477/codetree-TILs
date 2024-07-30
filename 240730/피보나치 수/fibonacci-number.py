import sys

N = int(sys.stdin.readline())

ls = [0 for _ in range(45)]
ls[0] = 1
ls[1] = 1
for i in range(2, N):
    ls[i] = ls[i-1] + ls[i-2]
    
print(ls[N-1])