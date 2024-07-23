import sys

N, M, K =   map(int, sys.stdin.readline().split())
apples = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
orders = [list(sys.stdin.readline().split()) for _ in range(K)]

def dist(dot1, dot2):
    x1, y1 = dot1
    x2, y2 = dot2
    return abs(x1-x2) + abs(y1-y2)

def in_range(dot):
    x, y = dot
    return 0 <= x <= N-1 and 0 <= y <= N-1

dir_dic = {'U': (0, -1), 'D': (0, 1), 'R': (1, 0), 'L': (-1, 0)}

head_y, head_x, tail_y, tail_x = 0, 0, 0, 0
now_snake_len = 1
T = 0
end = False
field = [[0 for _ in range(N)] for _ in range(N)]
for y, x in apples:
    field[y-1][x-1] = 'A'

for dir, num in orders:
    num = int(num)
    
    for _ in range(num):
        if T < 2:
            dx, dy = dir_dic[dir]
            if in_range((head_x+dx, head_y+dy)):
                if field[head_y+dy][head_x+dx] in dir_dic:
                    T += 1
                    end=True
                    break
                else:
                    field[head_y][head_x] = dir
                    field[head_y+dy][head_x+dx] = dir
                    head_x, head_y = head_x+dx, head_y+dy
                    T += 1
                    now_snake_len += 1
            else:
                T += 1
                end = True
                break
        
        else:
            dx, dy = dir_dic[dir]
            if in_range((head_x+dx, head_y+dy)):
                if field[head_y+dy][head_x+dx] != 'A':
                    tdx, tdy = dir_dic[field[tail_y][tail_x]]
                    field[tail_y][tail_x] = 0
                    tail_x, tail_y = tail_x + tdx, tail_y+tdy
                T += 1
                
                if field[head_y+dy][head_x+dx] in dir_dic:
                    end=True
                    break
                        
                field[head_y][head_x] = dir
                field[head_y+dy][head_x+dx] = dir
                head_x, head_y = head_x+dx, head_y+dy
            else:
                T += 1
                end = True
                break
        
        
    
    if end:
        break

print(T)