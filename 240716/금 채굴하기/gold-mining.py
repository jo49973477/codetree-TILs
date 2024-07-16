import sys

N, M = map(int, sys.stdin.readline().split()) # N*N줄 , 가격 M원
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def gold_n_cost(dot, K, f):
    x, y = dot
    dots_square = [(x+i, y+j) for i in range(-K, K+1) for j in range(-K+abs(i), K-abs(i)+1)]
    
    ans = 0
    cost = 0
    for (i, j) in dots_square:
        if 0 <= i <= N-1 and 0 <= j <= N-1:
            ans += f[i][j]
            cost += 1
            
    return ans, cost

max_gold = 0

for i in range(N):
    for j in range(N):
        for k in range(N):
            gold, cost = gold_n_cost((i, j), k, field)
            max_gold = max((max_gold, gold))if (M*gold - cost)>= 0 else max_gold

print(max_gold)