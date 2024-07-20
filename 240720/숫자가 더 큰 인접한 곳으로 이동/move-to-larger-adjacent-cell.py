import sys
import copy

N, r, c = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

r, c = r-1, c-1
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

result = [field[r][c], ]

while True:
    now = field[r][c]
    next_r, next_c = r, c

    for dx, dy in zip(dxs, dys):
        if 0 <= r+dy <= N-1 and 0 <= c+dx <= N-1:
            if field[r+dy][c+dx] > now:
                next_r, next_c = r+dy, c+dx
    
    if next_r == r and next_c == c:
        break
    else:
        r, c = next_r, next_c
        result.append(field[r][c])

print(' '.join(map(str, result)))