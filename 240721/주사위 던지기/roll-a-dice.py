import sys

N, M, r, c = map(int, sys.stdin.readline().split())
orders = sys.stdin.readline().split()

r, c = r-1, c-1
field = [[0 for _ in range(N)] for _ in range(N)]


now, L, R, D, U = 6, 4, 3, 2, 5
dir_dic = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

field[r][c] = now
for dir in orders:
    dy, dx = dir_dic[dir]
    if 0 <= r+dy <= N-1 and 0 <= c+dx <= N-1:
        if dir == 'L':
            now, L, R, D, U = L, 7-now, now, D, U
        elif dir == 'R':
            now, L, R, D, U = R, now, 7-now, D, U
        elif dir == 'D':
            now, L, R, D, U = D, L, R, 7-now, now
        elif dir == 'U':
            now, L, R, D, U = U, L, R, now, 7-now
        
        r, c = r+dy, c+dx
        field[r][c] = now

print(sum([sum(l) for l in field]))