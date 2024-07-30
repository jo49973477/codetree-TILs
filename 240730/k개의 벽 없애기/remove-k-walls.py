import sys
from collections import deque
from itertools import combinations

N, K = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
r1, c1 = map(int, sys.stdin.readline().split())
r2, c2 = map(int, sys.stdin.readline().split())
r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1

dys = [0, 0, -1, 1]
dxs = [1, -1, 0, 0]

ans = sys.maxsize

wall_list = []
for i in range(N):
    for j in range(N):
        if field[i][j] == 1:
            wall_list.append((i,j))
            
ans_candidates = []

for brokens in combinations(wall_list, K):
    for i, j in brokens:
        field[i][j] = 0
    
    visited = [[field[i][j] == 1 for j in range(N)] for i in range(N)]
    step = [[0 for _ in range(N)] for _ in range(N)]
    
    q = deque()
    q.append((r1, c1))
    
    while q:
        y, x = q.popleft()
        
        if (y, x) == (r2, c2):
            ans_candidates.append(step[y][x])
            break
        
        for dy, dx in zip(dys, dxs):
            if 0 <= y+dy <= N-1 and 0 <= x+dx <= N-1 and not visited[y+dy][x+dx]:
                step[y+dy][x+dx] = step[y][x] + 1
                visited[y+dy][x+dx] = True
                q.append((y+dy, x+dx))
            
    
    for i, j in brokens:
        field[i][j] = 1

print(min(ans_candidates) if ans_candidates else -1)