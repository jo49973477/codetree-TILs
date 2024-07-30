import sys
from collections import deque
#릴파누나가 좋아하는 귤 상하게 하지 마!
N, K = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dys = [0, 0, -1, 1]
dxs = [1, -1, 0, 0]

rotten = [[False for j in range(N)] for i in range(N)]
ans_field = [[-2 for _ in range(N)] for _ in range(N)]

q = deque()
for i in range(N):
    for j in range(N):
        if field[i][j] == 0:
            rotten[i][j] = True
            ans_field[i][j] = -1
        elif field[i][j] == 2: #상한귤이면
            rotten[i][j] = True
            ans_field[i][j] = 0
            q.append((i,j))
            
while q:
    y, x = q.popleft()
    for dy, dx in zip(dys, dxs):
        if 0 <= y+dy <= N-1 and 0 <= x+dx <= N-1 and not rotten[y+dy][x+dx]:
            rotten[y+dy][x+dx] = True
            ans_field[y+dy][x+dx] = ans_field[y][x] + 1
            q.append((y+dy,x+dx))

print('\n'.join([' '.join(map(str, l)) for l in ans_field]))