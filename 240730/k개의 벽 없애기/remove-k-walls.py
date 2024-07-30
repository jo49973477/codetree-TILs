import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
r1, c1 = map(int, sys.stdin.readline().split())
r2, c2 = map(int, sys.stdin.readline().split())
r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1

dys = [0, 0, -1, 1]
dxs = [1, -1, 0, 0]

q = deque()
q.append((r1, c1))

visited = [[False for j in range(N)] for i in range(N)]
step = [[0 for _ in range(N)] for _ in range(N)]
wall_step = [[0 for _ in range(N)] for _ in range(N)]

ans = -1

while q:
    y, x = q.popleft()
    
    if (y, x) == (r2, c2):
        ans = step[y][x]
        break
        
    if wall_step[y][x] > K:
        continue
        
        
    for dy, dx in zip(dys, dxs):
        if 0 <= y+dy <= N-1 and 0 <= x+dx <= N-1 and not visited[y+dy][x+dx]:
            visited[y+dy][x+dx] = True
            step[y+dy][x+dx] = step[y][x] + 1
            q.append((y+dy, x+dx))
            
            if field[y+dy][x+dx] == 1:
                wall_step[y+dy][x+dx] = wall_step[y][x] + 1
            else:
                wall_step[y+dy][x+dx] = wall_step[y][x]

print(ans)