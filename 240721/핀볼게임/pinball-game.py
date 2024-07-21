import sys

N = int(sys.stdin.readline())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dir_dic = {'U': (0, -1), 'D': (0, 1), 'R': (1, 0), 'L': (-1, 0)}

dic1 = {'D': 'L', 'L':'D', 'R': 'U', 'U':'R'}
dic2 = {'D': 'R', 'L':'U', 'R': 'D', 'U':'L'}

ans = 0

for i in range(N):
    start_dots = [(i, 0) , (0, i), (N-1, i), (i, N-1)]
    start_dirs = ['D', 'R', 'L', 'U']

    for start_dot, start_dir in zip(start_dots, start_dirs):
        move = 1
        x, y = start_dot
        dir = start_dir
        
        while True:
            if 0 <= x <= N-1 and 0 <= y <= N-1:
                now = field[y][x]
                dir = dic1[dir] if now == 1 else dic2[dir] if now == 2 else dir
                
                dx, dy = dir_dic[dir]
                x, y = x+dx, y+dy
                move += 1
            else:
                break
        
        ans = max((ans, move))

print(ans)