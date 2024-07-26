import sys

def dist(dot1, dot2):
    x1, y1 = dot1
    x2, y2 = dot2
    return (x1-x2)**2 + (y1-y2)**2

def dots_max(dots):
    max_val = 0 
    for i, dot1 in enumerate(dots):
        for j, dot2 in enumerate(dots[(i+1):]):
            max_val = max((dist(dot1, dot2), max_val))
    return max_val

N, M = map(int, sys.stdin.readline().split())
dots = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

min_val = sys.maxsize
def choose(depth, dots_arr, last_idx):
    if depth == M:
        dist = dots_max(dots_arr)
        global min_val
        min_val = min((min_val, dist))
        return
    else:
        for idx in range(last_idx + 1, N):
            dots_arr[depth] = dots[idx]
            choose(depth + 1, dots_arr, idx)

choose(0, [0 for _ in range(M)], -1)
print(min_val)