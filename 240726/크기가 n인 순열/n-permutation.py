import sys

def permu(depth, N, visited, arr):
    if depth == N:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(N):
        if visited[i]:
            continue
        else:
            visited[i] = True
            arr[depth] = i + 1
            permu(depth + 1, N, visited, arr)
            visited[i] = False

N = int(sys.stdin.readline())
permu(0, N, [False for _ in range(N)], [0 for _ in range(N)])