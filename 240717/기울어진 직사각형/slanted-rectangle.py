import sys

N = int(sys.stdin.readline())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

length_arr = []
for lens in range(2, N):
    length_arr += [(i, lens-i) for i in range(1, lens)]

ans = 0
for l, r in length_arr:
    for y_st in range(N-l-r):
        for x_st in range(N-l-r):
            dots = [(y_st+i, x_st+l-i) for i in range(l+1)] + [(y_st+r+i, x_st+r+l-i) for i in range(l+1)] #좌상단, 우하단
            dots += [(y_st+i, x_st+l+i) for i in range(1, r)] + [(y_st+l+i, x_st+i) for i in range(1, r)] #우상단, 좌하단
            
            rec_val = sum([field[i][j] for i, j in dots])
            ans = max((ans, rec_val))
            
            
print(ans)