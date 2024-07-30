import sys
from collections import deque
# 0 - movable , 1 - wall , 2 - human , 3 - destination
N, H, M = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dys = [0, 0, -1, 1]
dxs = [1, -1, 0, 0]

man_pos_list = []
for i in range(N):
    for j in range(N):
        if field[i][j] == 2:
            man_pos_list.append((i,j))

ans_field = [[0 for _ in range(N)] for _ in range(N)]

for pos in man_pos_list:
    q = deque()
    q.append(pos)
    ans = -1
    
    visited = [[field[i][j] == 1  for j in range(N)] for i in range(N)]
    step = [[0 for _ in range(N)] for _ in range(N)]
    
    while q:

        y, x = q.popleft()
        
        if field[y][x] == 3:
            ans = step[y][x]
            break
        
        for dy, dx in zip(dys, dxs):
            if 0 <= y+dy <= N-1 and 0 <= x+dx <= N-1 and not visited[y+dy][x+dx]:
                step[y+dy][x+dx] = step[y][x] + 1
                visited[y+dy][x+dx] = True
                q.append((y+dy, x+dx))
    
    pos_y, pos_x = pos
    ans_field[pos_y][pos_x] = ans
    
print('\n'.join([' '.join(map(str, l)) for l in ans_field]))