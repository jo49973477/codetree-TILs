import sys

N, M = map(int, sys.stdin.readline().split()) # N 이하 수 중 M개 수

def combination(depth, result):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    
    last_num = 0 if depth == 0 else result[depth-1]
    for num in range(last_num + 1, N + 1):
        result[depth] = num
        combination(depth + 1, result)
        
combination(0, [0 for _ in range(M)])