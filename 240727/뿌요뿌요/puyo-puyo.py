import sys

N = int(sys.stdin.readline())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

def bombcount(dot):
    i, j = dot
    move_arr = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    global visited
    visited[i][j] = True
    result = 1
    
    for next_i, next_j in move_arr:
        inrange = 0 <= next_i <= N-1 and 0 <= next_j <= N-1
        if inrange:
            
            sameregion = field[i][j] == field[next_i][next_j]
            if sameregion and not visited[next_i][next_j]:
                result += bombcount((next_i, next_j))
    
    return result

booms, maxblocks = 0, 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            blocks = bombcount((i,j))
            booms = booms+1 if blocks >= 4 else booms
            maxblocks = max((blocks, maxblocks))

print(booms, maxblocks)