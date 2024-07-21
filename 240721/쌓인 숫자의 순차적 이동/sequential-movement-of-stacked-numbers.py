import sys

N, M = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
orders = list(map(int, sys.stdin.readline().split()))

def move(result_field ,dot):
    y, x = dot
    dots = [(y+1, x-1), (y, x-1), (y-1, x-1), (y-1, x), (y+1, x), (y+1, x+1), (y, x+1), (y-1, x+1)]
    
    max_val = 0
    dot_move = ()
    for i, j in dots:
        if 0 <= i <= N-1 and 0 <= j <= N-1:
            val = max(result_field[N*i+j]) if result_field[N*i+j] else 0
            dot_move = (i, j) if val > max_val else dot_move
            max_val = max((max_val, val))
    
    return dot_move


field_dic = {}
for r in range(N):
    for c in range(N):
        field_dic[field[r][c]] = (r, c)

result = [[field[i//N][i%N]] for i in range(N**2)]


for num in orders:
    r, c = field_dic[num]
    move_dot = move(result, (r,c))
    
    if move_dot != ():
        move_r, move_c = move_dot
    
        idx = result[N*r+c].index(num)
        result[N*r+c], result[move_r*N+move_c] = result[N*r+c][(idx+1):], result[N*r+c][:(idx+1)] + result[move_r*N+move_c]
    
        for nu in result[N*r+c]:
            field_dic[nu] = (r,c)
        
        for nu in result[move_r*N+move_c]:
            field_dic[nu] = (move_r, move_c)
        
    else:
        continue
    

print('\n'.join([' '.join(map(str, l))if l else 'None' for l in result]))