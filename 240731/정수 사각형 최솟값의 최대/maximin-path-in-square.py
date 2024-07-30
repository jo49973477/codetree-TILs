import sys

N = int(sys.stdin.readline())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            field[i][j] = min(field[i][j], field[i][j-1])
        elif j == 0:
            field[i][j] = min(field[i][j], field[i-1][j])
        else:
            field[i][j] = max(min(field[i][j], field[i-1][j]), min(field[i][j], field[i][j-1]))

print(field[N-1][N-1])