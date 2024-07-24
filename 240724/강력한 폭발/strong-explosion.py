import sys



N = int(sys.stdin.readline())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def fucked_region_count(idx_list, val_list):
    count_field = [[0 for _ in range(N)] for _ in range(N)]
    
    for (i, j), type in zip(idx_list, val_list):
        dots = []
        if type == 1:
            dots = [(i-2, j), (i-1, j), (i, j), (i+1, j), (i+2, j)]
        elif type == 2:
            dots = [(i-1, j), (i+1, j), (i, j), (i, j-1), (i, j+1)]
        else:
            dots = [(i-1, j-1), (i+1, j-1), (i,j), (i-1, j+1), (i+1, j+1)]
        
        for (y, x) in dots:
            if 0 <= y <= N-1 and 0 <= x <= N-1:
                count_field[y][x] = 1
    return sum([sum(l) for l in count_field])

idx_list = []
for i in range(N):
    for j in range(N):
        if field[i][j]:
            idx_list.append((i,j))

ans = 0

def backtrack(depth, idx_list, val_list):
    if depth == len(idx_list):
        fucked = fucked_region_count(idx_list, val_list)
        global ans
        ans = max((ans, fucked))        
    else:
        for type in range(1, 4):
            val_list[depth] = type
            backtrack(depth + 1, idx_list, val_list)
            val_list[depth] = 0
        

backtrack(0, idx_list, [0 for _ in range(len(idx_list))])

print(ans)