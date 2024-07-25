import sys

K, N = map(int, sys.stdin.readline().split())

def back_track(depth, result):
    if depth == N:
        print(' '.join(map(str, result)))
    else:
        for num in range(1, K+1):
            if depth >= 2 and num == result[depth-1] == result[depth-2]:
                continue
            else:
                result[depth] = num
                back_track(depth + 1, result)
                
back_track(0, [0 for _ in range(N)])