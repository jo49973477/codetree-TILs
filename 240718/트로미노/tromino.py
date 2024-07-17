import sys

N, M = map(int, sys.stdin.readline().split()) # M열 N줄
f = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = 0
for i in range(N-1):
    for j in range(M-1):
        ans = max([ans, f[i][j] + f[i+1][j] + f[i][j+1], f[i][j] + f[i+1][j] + f[i+1][j+1],
                   f[i][j] + f[i][j+1] + f[i+1][j+1], f[i][j+1] + f[i+1][j] + f[i+1][j+1]])

for i in range(N):
    for j in range(M-2):
        ans = max([ans, f[i][j] + f[i][j+1] + f[i][j+2]])
        
for i in range(N-2):
    for j in range(M):
        ans = max([ans, f[i][j] + f[i+1][j] + f[i+2][j]])
        
print(ans)