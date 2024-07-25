import sys

N, M, K = map(int, sys.stdin.readline().split()) # K개 말, M개 판
yut_list = list(map(int, sys.stdin.readline().split())) # N개 윷

ans = 0

def backtrack(depth, pos_list):
    if depth == N:
        arrived = sum([1 if pos >= M else 0 for pos in pos_list])
        global ans
        ans = max((ans, arrived))
    else:
        all_arrived = True
        for mal in range(K):
            if pos_list[mal] >= M:
                continue
            else:
                all_arrived = False
                pos_list[mal] += yut_list[depth]
                backtrack(depth+1, pos_list)
                pos_list[mal] -= yut_list[depth]
        
        if all_arrived:
            backtrack(N, pos_list)
                

backtrack(0, [1 for _ in range(K)])
print(ans)