import sys
from collections import deque

N = int(sys.stdin.readline())
r_st, c_st, r_end, c_end = map(int, sys.stdin.readline().split())
r_st, c_st, r_end, c_end = r_st-1, c_st-1, r_end-1, c_end-1

dys = [1, 1, -1, -1, 2, -2, 2, -2]
dxs = [2, -2, 2, -2, 1, 1, -1, -1]

visited = [[False for _ in range(N)] for _ in range(N)]
step = [[0 for _ in range(N)] for _ in range(N)]
visited[r_st][c_st] = 1
q = deque()
q.append((r_st, c_st))

while q:
    y, x = q.popleft()
    
    if (y,x) == (r_end, c_end):
        break
    
    for dy, dx in zip(dys, dxs):
        if 0 <= y+dy <= N-1 and 0 <= x+dx <= N-1 and not visited[y+dy][x+dx]:
            step[y+dy][x+dx] = step[y][x] + 1
            visited[y+dy][x+dx] = True
            q.append((y+dy, x+dx))
            
print(step[r_end][c_end] if step[r_end][c_end] != 0 else -1)