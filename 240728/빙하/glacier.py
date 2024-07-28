import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dys = [0, 0, -1, 1]
dxs = [1, -1, 0, 0]

isGlacier = True
fucked = 0
T = 0
while isGlacier:
    q = deque()
    q.append((0,0))
    visited = [[field[i][j] == 1 for j in range(M)] for i in range(N)]
    visited[0][0] = True
    
    T += 1
    melted = 0
    
    while q:
        y, x = q.popleft()
                
        for dy, dx in zip(dys, dxs):
            if 0 <= y+dy <= N-1 and 0 <= x+dx <= M-1:
                if not visited[y+dy][x+dx]:
                    visited[y+dy][x+dx] = True
                    q.append((y+dy, x+dx))
                elif field[y+dy][x+dx] == 1:
                    field[y+dy][x+dx] = 0
                    melted += 1
    
    if sum([sum(l) for l in field]) == 0:
        isGlacier = False
        fucked = melted
                    

print(T, fucked)