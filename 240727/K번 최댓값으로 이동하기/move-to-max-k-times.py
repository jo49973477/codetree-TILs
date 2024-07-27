from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
r, c = map(int, sys.stdin.readline().split())
r, c = r-1, c-1

dys = [0, 0, -1, 1]
dxs = [1, -1, 0, 0]

for _ in range(K):
    now_val = field[r][c]
    q = deque()
    q.append((r,c))
    
    visited = [[field[i][j] >= now_val for j in range(N)]for i in range(N)]
    visited[r][c] = True
    
    next_r, next_c, max_val = r, c, 0
    
    while q:
        y, x = q.popleft()
        
        if field[y][x] > max_val and (y, x) != (r, c):
            max_val = field[y][x]
            next_r, next_c = y, x
        elif field[y][x] == max_val:
            if y < next_r or (y == next_r and x < next_c):
                max_val = field[y][x]
                next_r, next_c = y, x
            
        
        for dy, dx in zip(dys, dxs):
            if 0 <= y+dy <= N-1 and 0 <= x+dx <= N-1 and not visited[y+dy][x+dx]:
                visited[y+dy][x+dx] = True
                q.append((y+dy, x+dx))

    
    r, c = next_r, next_c

print(r+1, c+1)