import sys
from collections import deque
from itertools import combinations

N, K, u, d = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dys = [0, 0, -1, 1]
dxs = [1, -1, 0, 0]

all_dots = [(num//N, num%N) for num in range(0, N**2)]

ans = 0

for dots in combinations(all_dots, K):
    
    visited = [[False for _ in range(N)] for _ in range(N)]
    q = deque()
    for dot in dots:
        q.append(dot)
        y, x = dot
        visited[y][x] = True
    
    cities = 0
    while q:
        y, x = q.popleft()
        cities += 1
        
        for dy, dx in zip(dys, dxs):
            if 0 <= y+dy <= N-1 and 0 <= x+dx <= N-1 and not visited[y+dy][x+dx]:
                visited[y+dy][x+dx] = True
                if u <= abs(field[y+dy][x+dx]-field[y][x]) <= d:
                    q.append((y+dy, x+dx))
    
    ans = max((ans, cities))

print(ans)