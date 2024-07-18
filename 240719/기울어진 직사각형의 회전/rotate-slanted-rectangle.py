REVERSECLOCK = 0
CLOCK = 1
import sys
import copy

N = int(sys.stdin.readline())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
y, x, m1, m2, m3, m4, dir = map(int, sys.stdin.readline().split())

y, x = y-1, x-1
f = copy.deepcopy(field)

if dir == REVERSECLOCK:
    for i in range(m1):
        field[y-i-1][x+i+1] = f[y-i][x+i]
    
    y, x = y-m1, x+m1
    for i in range(m2):
        field[y-i-1][x-i-1] = f[y-i][x-i]
    
    y, x = y-m2, x-m2
    for i in range(m3):
        field[y+i+1][x-i-1] = f[y+i][x-i]
    
    y, x = y+m3, x-m3
    for i in range(m4):
        field[y+i+1][x+i+1] = f[y+i][x+i]
        
        
elif dir == CLOCK:
    for i in range(m1):
        field[y-i][x+i] = f[y-i-1][x+i+1]
    
    y, x = y-m1, x+m1
    for i in range(m2):
        field[y-i][x-i] = f[y-i-1][x-i-1]
    
    y, x = y-m2, x-m2
    for i in range(m3):
        field[y+i][x-i] = f[y+i+1][x-i-1]
    
    y, x = y+m3, x-m3
    for i in range(m4):
        field[y+i][x+i] = f[y+i+1][x+i+1]
        
print('\n'.join([' '.join(map(str, line)) for line in field]))