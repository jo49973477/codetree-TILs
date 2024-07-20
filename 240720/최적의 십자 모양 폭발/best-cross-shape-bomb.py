import sys
import copy

def boom(bombs, dot):
    x, y = dot
    new_bombs = copy.deepcopy(bombs)
    N = len(bombs)
    
    bomb_dots = [(x,y)]
    for i in range(1, bombs[y][x]):
        bomb_dots.append((x-i, y))
        bomb_dots.append((x+i, y))
        bomb_dots.append((x, y-i))
        bomb_dots.append((x, y+i))
        
    for j, i in bomb_dots:
        if 0 <= i <= N-1 and 0 <= j <= N-1:
            new_bombs[i][j] = 0
    
    return new_bombs    

def nomuhyeon(bombs):
    N = len(bombs)
    new_bombs = [[0 for _ in range(N)] for _ in range(N)]
    
    for col in range(N):
        last = N-1
        for row in range(N-1, -1, -1):
            if bombs[row][col] == 0:
                continue
            else:
                new_bombs[last][col] = bombs[row][col]
                last -= 1
    
    return new_bombs

def pairs(bombs):
    N = len(bombs)
    
    pair = 0
    for col in range(N):
        for row in range(1, N):
            if bombs[row][col] == 0:
                continue
            elif bombs[row-1][col] == bombs[row][col]:
                pair += 1
            
    for row in range(N):
        for col in range(1, N):
            if bombs[row][col] == 0:
                continue
            elif bombs[row][col-1] == bombs[row][col]:
                pair += 1
                
    return pair

N = int(sys.stdin.readline())
bombs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        exploded_bombs = nomuhyeon(boom(bombs, (i,j)))
        ans = max((ans, pairs(exploded_bombs)))
        
print(ans)