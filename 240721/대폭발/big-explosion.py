import sys
import copy


N, M, r, c = map(int, sys.stdin.readline().split())

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
field = [[0 for _ in range(N)] for _ in range(N)]
field[r-1][c-1] = 1

for _ in range(M):
    new_field = copy.deepcopy(field)
    
    for y in range(N):
        for x in range(N):
            if field[y][x] == 1:
                for dx, dy in zip(dxs, dys):
                    if 0 <= x+dx <= N-1 and 0 <= y+dy <= N-1:
                        new_field[y+dy][x+dx] = 1
    
    dxs = [dx*2 for dx in dxs]
    dys = [dy*2 for dy in dys]
    field = new_field
    
print(sum([sum(l) for l in field]))