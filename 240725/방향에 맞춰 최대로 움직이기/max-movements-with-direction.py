import sys

N = int(sys.stdin.readline())
square = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dirs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
pos_first = tuple(map(int, sys.stdin.readline().split()))
y, x = pos_first
pos_first = (y-1, x-1)
dir_dic = {1: (0, -1), 2: (1, -1), 3: (1, 0), 4: (1, 1), 5: (0, 1), 6:(-1, 1), 7:(-1, 0), 8: (-1, -1)}

ans = 0

def move(pos, num):
    y, x = pos
    dx, dy = dir_dic[dirs[y][x]]
    now_val = square[y][x]
    
    can_move = []
    while True:
        if 0 <= y+dy <= N-1 and 0 <= x+dx <= N-1:
            if square[y+dy][x+dx] > now_val:
                can_move.append((y+dy, x+dx))
            y, x = y+dy, x+dx
        else:
            break
    
        
    if can_move:
        for new_pos in can_move:
            move(new_pos, num+1)
    else:
        global ans
        ans = max((ans, num))

move(pos_first, 0)
print(ans)