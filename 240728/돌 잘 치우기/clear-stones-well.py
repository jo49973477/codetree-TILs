import sys
from collections import deque
from itertools import combinations

N, K, M = map(int, sys.stdin.readline().split()) # N은 그거개스 K는 점 개수 M은 돌개수
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dots = [tuple(map(int, sys.stdin.readline().split())) for _ in range(K)]

dys = [1, -1, 0, 0]
dxs = [0, 0, 1, -1]

visited = [[False for _ in range(N)] for _ in range(N)]
rm_stone_candidates = []

q = deque()
for y, x in dots:
    q.append((y-1, x-1))
    visited[y-1][x-1] = True

while q:
    y, x = q.popleft()
    
    for dy, dx in zip(dys, dxs):
        if 0 <= y+dy <= N-1 and 0 <= x+dx <= N-1 and not visited[y+dy][x+dx]:
            visited[y+dy][x+dx] = True
            if field[y+dy][x+dx] == 1: #돌이면
                rm_stone_candidates.append((y+dy,x+dx))
            elif field[y+dy][x+dx] == 0: #돌 아니면
                q.append((y+dy, x+dx))

ans = 0

for rm_stones in combinations(rm_stone_candidates, M):
    for y, x in rm_stones: #돌치우고
        field[y][x] = 0
    
    visited = [[field[i][j] == 1 for j in range(N)] for i in range(N)]
    
    q = deque()
    for y, x in dots:
        q.append((y-1, x-1))
        visited[y-1][x-1] = True
    
    movables = 0
    while q:
        y, x = q.popleft()
        movables += 1
        
        for dy, dx in zip(dys, dxs):
            if 0 <= y+dy <= N-1 and 0 <= x+dx <= N-1 and not visited[y+dy][x+dx]:
                q.append((y+dy, x+dx))
                visited[y+dy][x+dx] = True
    
    ans = max((ans, movables))
    
    for y, x in rm_stones: #돌 다시 생김
        field[y][x] = 1

print(ans)