import sys

def move(field ,dot):
    N = len(field)
    x, y = dot
    dots = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    
    max_val = 0
    dot_move = ()
    for j, i in dots:
        if 0 <= i <= N-1 and 0 <= j <= N-1:
            dot_move = (j, i) if field[i][j] >= max_val else dot_move
            max_val = max((max_val, field[i][j]))
    
    return dot_move
    


N, M, T = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
marvels = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

marvel_field = [[0 for _ in range(N)] for _ in range(N)]

for y, x in marvels:
    y, x = y-1, x-1
    marvel_field[y][x] = 1

for _ in range(T):
    
    new_marvel_field = [[0 for _ in range(N)] for _ in range(N)]
    
    for y in range(N):
        for x in range(N):
            if marvel_field[y][x] == 1:
                move_x, move_y = move(field, (x,y))
                new_marvel_field[move_y][move_x] += 1
    
    for y in range(N):
        for x in range(N):
            new_marvel_field[y][x] = 0 if new_marvel_field[y][x] > 1 else new_marvel_field[y][x]
            
    marvel_field = new_marvel_field

print(sum([sum(l) for l in marvel_field]))