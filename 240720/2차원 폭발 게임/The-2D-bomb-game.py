import sys

def boom(bombs, M):
    N = len(bombs)
    
    for col in range(N):
        repeat = 1
        for row in range(N):
            if row == N-1 or bombs[row][col] != bombs[row+1][col]:
                if repeat >= M:
                    for i in range(repeat):
                        bombs[row-i][col] = 0
                repeat = 1
            elif bombs[row][col] == bombs[row+1][col]:
                repeat += 1
    
    return bombs

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

def rotate(bombs):
    N = len(bombs)
    new_bombs = [[0 for _ in range(N)] for _ in range(N)]
    
    for row in range(N):
        for col in range(N):
            new_bombs[col][N-1-row] = bombs[row][col]
    return new_bombs

def count_bombs(bombs):
    N = len(bombs)
    ans = 0
    for row in range(N):
        for col in range(N):
            ans = ans + 1 if bombs[row][col] != 0 else ans
    
    return ans

N, M, K = map(int, sys.stdin.readline().split())
bombs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for _ in range(K):
    bombs = boom(bombs, M)
    bombs = nomuhyeon(bombs)
    bombs = rotate(bombs)
    bombs = nomuhyeon(bombs)
    bombs = boom(bombs, M)
    

print(count_bombs(bombs))