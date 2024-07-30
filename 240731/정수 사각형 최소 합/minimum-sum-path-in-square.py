import sys

N = int(sys.stdin.readline())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    for j in range(N-1, -1, -1):
        prev_dots = [(i-1, j), (i, j+1)]
        max_candidate = []
        for y, x in prev_dots:
            if 0 <= y <= N-1 and 0 <= x <= N-1:
                max_candidate.append(field[i][j] + field[y][x])
        
        if max_candidate:
            field[i][j] = min(max_candidate)

     
print(field[N-1][0])