import sys
sys.setrecursionlimit(30000)

N = int(sys.stdin.readline())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def in_range(y, x):
    return 0 <= y <= N-1 and 0 <= x <= N-1

dp = [[-1 for _ in range(N)] for _ in range(N)]
dys = [0, 0, -1, 1]
dxs = [-1, 1, 0, 0]

def count(dot):
    global dp
    y, x = dot
    
    if dp[y][x] != -1:
        return dp[y][x]
    
    ans_candidates = [1]
    for dy, dx in zip(dys, dxs):
        if in_range(y+dy, x+dx) and field[y+dy][x+dx] > field[y][x]:
            ans_candidates.append(1+count((y+dy, x+dx)))
    ans = max(ans_candidates)
    dp[y][x] = ans
    return ans

ans = 0
for i in range(N):
    for j in range(N):
        val = count((i,j))
        ans = max((ans, val))

print(ans)