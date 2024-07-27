import sys

N, M = map(int, sys.stdin.readline().split()) #가로 M 세로 N
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]


def areacount(dot):
    i, j = dot
    move_arr = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    global visited
    visited[i][j] = True
    
    for next_i, next_j in move_arr:
        if 0 <= next_i <= N-1 and 0 <= next_j <= M-1 and not visited[next_i][next_j]:
            areacount((next_i, next_j))
    
    return

max_height = max([max(l) for l in field])

ans_K, ans_areas = 0, -1
for K in range(1, max_height):
    visited = [[field[i][j] <= K for j in range(M)] for i in range(N)]
    
    areas_now = 0
    
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                areacount((i,j))
                areas_now += 1
    
    if areas_now > ans_areas:
        ans_K, ans_areas = K, areas_now
        print(K)

print(ans_K, ans_areas)