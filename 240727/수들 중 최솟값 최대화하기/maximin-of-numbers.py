import sys

N = int(sys.stdin.readline())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = 0

def permu(depth, visited, arr):
    if depth == N:
        result = min([field[i][j] for i, j in enumerate(arr)])
        global ans
        ans = max((ans, result))
        return
    
    for i in range(N):
        if visited[i]:
            continue
        else:
            visited[i] = True
            arr[depth] = i
            permu(depth + 1, visited, arr)
            visited[i] = False

permu(0, [False for _ in range(N)], [0 for _ in range(N)])
print(ans)