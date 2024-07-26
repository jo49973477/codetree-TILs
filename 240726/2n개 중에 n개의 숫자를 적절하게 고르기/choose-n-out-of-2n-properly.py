import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_list_sum = sum(num_list)

min_sub = sys.maxsize
def choose(depth, part_list, last_idx):
    if depth == N:
        set1, set2 = sum(part_list), num_list_sum - sum(part_list)
        global min_sub
        
        min_sub = min((abs(set1-set2), min_sub))
        return
    
    for idx in range(last_idx + 1, 2*N):
        part_list[depth] = num_list[idx]
        choose(depth + 1, part_list, idx)

choose(0, [0 for _ in range(N)], -1)
print(min_sub)