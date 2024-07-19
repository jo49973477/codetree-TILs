import sys
import copy

N = int(sys.stdin.readline())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
y, x = map(int, sys.stdin.readline().split())

y, x = y-1, x-1
explode_dots = [(y, x)]
for i in range(1, field[y][x]):
    explode_dots.append((y-i, x))
    explode_dots.append((y+i, x))
    explode_dots.append((y, x-i))
    explode_dots.append((y, x+i)) # 쓔1발 내가 이렇게 더럽게 써야 해?ㅜㅜ
    

for i, j in explode_dots:
    if 0 <= i <= N-1 and 0 <= j <= N-1:
        field[i][j] = 0

new_field = [[0 for _ in range(N)] for _ in range(N)]
for col in range(N):
    last = N-1    
    for row in range(N-1, -1, -1):
        if field[row][col] != 0:
            new_field[last][col] = field[row][col]
            last -= 1

print('\n'.join([' '.join(map(str, line)) for line in new_field]))