import sys

def backtracking(depth,K, N, result):
    if depth == N:
        print(' '.join(map(str, result)))
        return
    else:
        for num in range(1, K+1):
            result[depth] = num
            backtracking(depth+1, K, N, result)
            result[depth] = 0

K, N = map(int, sys.stdin.readline().split())

result = [0 for _ in range(N)]
backtracking(0, K, N, result)