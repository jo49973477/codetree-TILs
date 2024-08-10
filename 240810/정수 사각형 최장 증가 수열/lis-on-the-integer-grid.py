N = int(input())
matrix = [
    list(map(int, input().split()))
    for _ in range(N)
]

# dp[i][j] = (i, j) 부터 시작하는 최대 이동 거리
dp = [[0] * N for _ in range(N)]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def travel(x, y, move_cnt):
    if dp[x][y]:
        return dp[x][y]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    max_move_cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if in_range(nx, ny) and matrix[nx][ny] > matrix[x][y]:
            max_move_cnt = max(max_move_cnt, move_cnt + travel(nx, ny, move_cnt))

    # print(x, y, max_move_cnt)
    dp[x][y] = max_move_cnt
    return max_move_cnt


for i in range(N):
    for j in range(N):
        if not dp[i][j]:
            travel(i, j, 1)

print(max(map(max, dp))+1)