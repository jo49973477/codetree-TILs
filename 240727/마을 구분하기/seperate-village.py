import sys

N = int(sys.stdin.readline())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [[field[i][j] == 0 for j in range(N)] for i in range(N)]

def towncount(dot):
    i, j = dot
    move_arr = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    global visited
    visited[i][j] = True
    result = 1
    
    for next_i, next_j in move_arr:
        if 0 <= next_i <= N-1 and 0 <= next_j <= N-1 and not visited[next_i][next_j]:
            result += towncount((next_i, next_j))
    
    return result

town_num = 0
people_nums = []

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            people_num = towncount((i,j))
            people_nums.append(people_num)
            town_num += 1
people_nums.sort()

print(town_num)
print('\n'.join(map(str, people_nums)))