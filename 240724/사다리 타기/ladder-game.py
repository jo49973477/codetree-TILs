import sys

N, M = map(int, sys.stdin.readline().split())
ladders = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

def ghost_leg(ladders):
    ladders_dic = {}
    a_pos = [i+1 for i in range(N)]
    
    b_max = 0
    for a, b in ladders:
        b_max = max((b, b_max))
        if b in ladders_dic:
            ladders_dic[b].append(a)
        else:
            ladders_dic[b] = [a]
    
    for b in range(1, b_max + 1):
        if b in ladders_dic:
            for i in range(N):
                if a_pos[i] in ladders_dic[b]:
                    a_pos[i] += 1
                elif a_pos[i]-1 in ladders_dic[b]:
                    a_pos[i] -= 1
        else:
            continue
    
    return a_pos

ghost_leg_result = ghost_leg(ladders)

ans = len(ladders)

def backtrack(depth, put):
    if depth == M:
        ladders_now = [ladders[i] for i in range(M) if put[i]]
        if ghost_leg_result == ghost_leg(ladders_now):
            global ans
            ans = min((len(ladders_now), ans))
    else:
        put[depth] = True
        backtrack(depth+1, put)
        put[depth] = False
        backtrack(depth+1, put)

backtrack(0, [False for _ in range(M)])
print(ans)