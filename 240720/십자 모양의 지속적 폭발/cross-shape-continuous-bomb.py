import sys

N, M = map(int, sys.stdin.readline().split())
bombs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
boom_cols = [int(sys.stdin.readline()) for _ in range(M)]

for boom_col in boom_cols:
    boom_col -= 1
    boom_row = 0
    for i in range(N):
        if bombs[i][boom_col] != 0:
            boom_row = i
            break
    
    dots = [(boom_row, boom_col)]
    for i in range(1, bombs[boom_row][boom_col]):
        dots.append((boom_row - i, boom_col))
        dots.append((boom_row + i, boom_col))
        dots.append((boom_row, boom_col - i))
        dots.append((boom_row, boom_col + i))
    
    for y, x in dots:
        if 0 <= y <= N-1 and 0 <= x <= N-1:
            bombs[y][x] = 0
    
    new_bombs = [[0 for _ in range(N)] for _ in range(N)]
    for c in range(N):
        last = N-1
        for r in range(N-1, -1, -1):
            if bombs[r][c] == 0:
                continue
            else:
                new_bombs[last][c] = bombs[r][c]
                last -= 1
    
    bombs = new_bombs

print('\n'.join([' '.join(map(str, l)) for l in bombs]))