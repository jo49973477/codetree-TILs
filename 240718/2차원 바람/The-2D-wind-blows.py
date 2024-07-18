import sys
import copy

N, M, Q = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
order = [tuple(map(int, sys.stdin.readline().split())) for _ in range(Q)]

for t, l, b, r in order:
    l, t, r, b = l-1, t-1, r-1, b-1
    f1 = copy.deepcopy(field)

    field[t][(l+1):(r+1)]= f1[t][l:r]
    field[b][l:r]= f1[b][(l+1):(r+1)]
    
    for i in range(t, b):
        field[i][l] = f1[i+1][l]
        field[i+1][r] = f1[i][r]
    
    f2 = copy.deepcopy(field)
    
    for x in range(l, r+1):
        for y in range(t, b+1):
            dots = [(x, y) , (x-1, y), (x+1,y), (x, y-1), (x, y+1)]
            inran = [((0<= j <= M-1) and (0 <= i <= N-1)) for j, i in dots]
            
            dots_sum = sum([f2[i][j] if inran[idx] else 0 for idx ,(j, i) in enumerate(dots)])
            field[y][x] = dots_sum // sum(inran)
            

print('\n'.join([' '.join(map(str, line)) for line in field]))