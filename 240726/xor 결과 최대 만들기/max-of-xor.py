import sys


N, M = map(int, sys.stdin.readline().split()) # N 이하 수 중 M개 수
num_list = list(map(int, sys.stdin.readline().split()))

max_val = 0
def choose(depth, indexes):
    if depth == M:
        val = 0
        for i, idx in enumerate(indexes):
            if i == 0:
                val = num_list[idx]
            else:
                val ^= num_list[idx]
                
        global max_val
        max_val = max((max_val, val))
        return
    
    last_num = -1 if depth == 0 else indexes[depth-1]
    for num in range(last_num + 1, N):
        indexes[depth] = num
        choose(depth + 1, indexes)

choose(0, [0 for _ in range(M)])
print(max_val)