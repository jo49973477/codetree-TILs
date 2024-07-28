import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [[field[i][j] == 0 for j in range(M)] for i in range(N)]
step = [[0 for _ in range(M)] for _ in range(N)]

dys = [0, 0, -1, 1]
dxs = [1, -1, 0, 0]

q = deque()
q.append((0,0))

while q:
    y, x = q.popleft()
    
    for dy, dx in zip(dys, dxs):
        if 0 <= y+dy <= N-1 and 0 <= x+dx <= M-1 and not visited[y+dy][x+dx]:
            step[y+dy][x+dx] = step[y][x] + 1
            visited[y+dy][x+dx] = True
            q.append((y+dy, x+dx))

print(step[N-1][M-1] if step[N-1][M-1] != 0 else -1)