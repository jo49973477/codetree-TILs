from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split()) #가로 M 세로 N
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dots = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

visited = [[field[i][j] == 1 for j in range(N)] for i in range(N)]

dys = [0, 0, -1, 1]
dxs = [1, -1, 0, 0]

q = deque()
for y, x in dots:
    y, x = int(y)-1, int(x)-1
    visited[y][x] = True
    q.append((y,x))

ans = 0
while q:
    y, x = q.popleft()
    ans += 1

    for dy, dx in zip(dys, dxs):
        if 0 <= y+dy <= N-1 and 0 <= x+dx <= N-1 and not visited[y+dy][x+dx]:
            q.append((y+dy, x+dx))
            visited[y+dy][x+dx] = True

print(ans)