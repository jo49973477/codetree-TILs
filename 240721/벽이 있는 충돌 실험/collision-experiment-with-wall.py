import sys

T = int(sys.stdin.readline())

dir_dic = {'U': (0, -1), 'D': (0, 1), 'R': (1, 0), 'L': (-1, 0)}
chdir_dic = {'U': 'D', 'D': 'U', 'R':'L', 'L':'R'}

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    orders = [sys.stdin.readline().split() for _ in range(M)]
    orders = [(int(y)-1, int(x)-1, dir) for y, x, dir in orders]
    
    field = [[0 for _ in range(N)] for _ in range(N)]
    dir_field = [[0 for _ in range(N)] for _ in range(N)]
    
    for y, x, dir in orders:
        field[y][x] = 1
        dir_field[y][x] = dir
    
    for _ in range(2*N+2):
        new_field = [[0 for _ in range(N)] for _ in range(N)]
        new_dir_field = [[0 for _ in range(N)] for _ in range(N)]
        
        for y in range(N):
            for x in range(N):
                if field[y][x] == 1:
                    dir = dir_field[y][x]
                    dx, dy = dir_dic[dir]
                    
                    if 0 <= x+dx <= N-1 and 0 <= y+dy <= N-1:
                        new_field[y+dy][x+dx] += 1
                        new_dir_field[y+dy][x+dx] = dir
                    else:
                        new_field[y][x] += 1
                        new_dir_field[y][x] = chdir_dic[dir]
        
        
        for y in range(N):
            for x in range(N):
                if new_field[y][x] > 1:
                    new_field[y][x] = 0
                    new_dir_field[y][x] = 0
        
        field = new_field
        dir_field = new_dir_field
    
    balls = sum([sum(l) for l in field])
    print(balls)