import sys


N = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split()))

max_move = [-1 for _ in range(N)]
max_move[0] = 0

for check in range(N):
    candidates = []
    for j in range(check):
        if j + road[j] >= check:
            candidates.append(max_move[j] + 1)
    
    max_move[check] = max(candidates) if candidates else 0
    
print(max_move[-1])