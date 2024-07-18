import sys
import copy

def windofchange(row, dir, field):
    if dir == 'L':
        field[row] = [field[row][-1]] + field[row][:-1]
    elif dir == 'R':
        field[row] = field[row][1:] + [field[row][0]]
    
    return field

N, M, Q = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
order = [list(sys.stdin.readline().split()) for _ in range(Q)]

for row, dir in order:
    row = int(row) - 1
    field = windofchange(row, dir, field)
    
    d = dir
    for r in range(row+1, N):
        if sum([1 if field[r-1][i] == field[r][i] else 0 for i in range(M)]) > 0:
            d = 'R' if d == 'L' else 'L'
            field = windofchange(r, d, field)
        else:
            break
    
    d = dir
    for r in range(row-1, -1, -1):
        if sum([1 if field[r+1][i] == field[r][i] else 0 for i in range(M)]) > 0:
            d = 'R' if d == 'L' else 'L'
            field = windofchange(r, d, field)
        else:
            break
        
print('\n'.join([' '.join(map(str, line)) for line in field]))