import sys
def move(field ,dot):
    N = len(field)
    x, y = dot
    dots = [(x+1, y-1), (x, y-1), (x-1, y-1), (x-1, y), (x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1)]
    
    max_val = 0
    dot_move = ()
    for j, i in dots:
        if 0 <= i <= N-1 and 0 <= j <= N-1:
            dot_move = (j, i) if field[i][j] >= max_val else dot_move
            max_val = max((max_val, field[i][j]))
    
    return dot_move

N, M = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

pos_dic = {} #making dic about position
for x in range(N):
    for y in range(N):
        pos_dic[field[y][x]] = (x, y)

for _ in range(M):
    for num in range(1, N**2+1):
        x, y = pos_dic[num]
        
        swap_x, swap_y = move(field, (x,y))
        pos_dic[field[swap_y][swap_x]] = (x, y) 
        pos_dic[field[y][x]] = (swap_x, swap_y)
        field[y][x], field[swap_y][swap_x] = field[swap_y][swap_x], field[y][x]

print('\n'.join([' '.join(map(str,l)) for l in field]))