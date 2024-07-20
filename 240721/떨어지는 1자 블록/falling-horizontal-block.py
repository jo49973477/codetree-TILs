import sys

N, m, k = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

k = k-1 #씨1발 0번부터 달라고 미1친놈들아

insert_row = -1
for row in range(N):
    if sum(field[row][k:(k+m)]) == 0:
        insert_row += 1
    else:
        break

for col in range(k, k+m):
    field[insert_row][col] = 1

print('\n'.join([' '.join(map(str, l)) for l in field]))