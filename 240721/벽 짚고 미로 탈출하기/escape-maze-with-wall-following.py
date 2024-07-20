import sys

N = int(sys.stdin.readline())
y, x = map(int, sys.stdin.readline().split())
field = [sys.stdin.readline().strip() for _ in range(N)]


x, y = x-1, y-1
initial_x, initial_y = x, y
dxs, dys = [-1, 0, 1, 0] , [0, -1, 0, 1]

idx = 2
T = 0
rotate = 0
while True:
    dx, dy = dxs[idx], dys[idx] #앞으로갈길
    bx, by = dxs[(idx+1)%4], dys[(idx+1)%4] #바닥위치


    
    if rotate > 0 and rotate == 4 and (T > 0 and x == initial_x and y == initial_y):
        T = -1
        break
    elif 0 <= x <= N-1 and 0 <= y <= N-1:
        if 0 <= x+dx <= N-1 and 0 <= y+dy <= N-1 and field[y+dy][x+dx] == '#': #막히면
            idx = idx - 1 if idx != 0 else 3 #방향틀기
            rotate += 1
        elif field[y+by][x+bx] == '.': #아래에 바닥없으면
            rotate += 1
            idx = (idx+1)%4 #또 방향틀기
            x, y = x+bx, y+by #방향틀어서 전진
            T += 1
        elif field[y+by][x+bx] == '#': #아래에 바닥이 있다?
            rotate = 0
            x, y = x+dx, y+dy
            T += 1 #전진!
    else:
        break

print(T)