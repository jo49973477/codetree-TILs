import sys

N = int(sys.stdin.readline())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
step = [[1 for _ in range(N)] for _ in range(N)]

dys = [0, 0, -1, 1]
dxs = [1, -1, 0, 0]

for x in range(N):
    for y in range(N):
        for dy, dx in zip(dys, dxs):
            in_range = 0 <= x+dx <= N-1 and 0 <= y+dy <= N-1
            if in_range and field[y+dy][x+dx] > field[y][x]:
                step[y+dy][x+dx] = max((step[y][x]+1, step[y+dy][x+dx]))


max_val = max([max(l) for l in step])
print(max_val)