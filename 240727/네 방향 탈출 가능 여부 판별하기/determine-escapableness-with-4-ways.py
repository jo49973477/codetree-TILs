from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split()) #가로 M 세로 N
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[field[i][j] == 0 for j in range(M)] for i in range(N)]
visited[0][0] = True

dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]

ans = 0
q = deque()
q.append((0,0))

while q:
    y, x = q.popleft()
    
    if y == N-1 and x == N-1:
        ans = 1
        break
    
    for dy, dx in zip(dys, dxs):
        if 0 <= y+dy <= N-1 and 0 <= x+dx <= N-1 and not visited[y+dy][x+dx]:
            q.append((y+dy, x+dx))
            visited[y+dy][x+dx] = True

print(ans)