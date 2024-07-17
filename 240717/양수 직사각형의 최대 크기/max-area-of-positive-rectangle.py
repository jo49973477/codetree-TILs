import sys

N, M = map(int, sys.stdin.readline().split()) # N 세로 M 가로
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
field_plus = [[1 if var >= 0 else 0  for var in line] for line in field]

dots = []

for i in range(N-1):
    for j in range(i+1, N):
        for k in range(M-1):
            for l in range(k+1, M):
                dots.append((i,j,k,l))

ans = -1
for t, b, l, r in dots:
    field_plus_sum = sum([sum(line[l:r+1]) for line in field_plus[t:b+1]])
    if field_plus_sum == ((b-t+1)*(r-l+1)):
        ans = max((ans, field_plus_sum))

print(ans)