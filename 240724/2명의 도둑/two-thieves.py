import sys
import copy

N, M, C = map(int, sys.stdin.readline().split())
goods = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


put_list = []
def backtrack(depth, put):
    if depth == M:
        global put_list
        my_put = copy.deepcopy(put)
        put_list.append(my_put)
    else:
        put[depth] = True
        backtrack(depth+1, put)
        put[depth] = False
        backtrack(depth+1, put)
        
backtrack(0, [False for _ in range(M)])

pos_list = []
for i in range(N):
    for j in range(N-M+1):
        for y in range(i, N):
            for x in range(N-M+1):
                if (y == i and x >= j+M) or (y > i):
                    pos_list.append([(i,j),(y,x)])


max_val = 0
for (y1, x1), (y2, x2) in pos_list:
    max1 = 0
    range1 = goods[y1][x1:(x1+M)]
    if sum(range1) <= C:
        max1 = sum([x**2 for x in range1])
    else:
        for put in put_list:
            if sum([range1[i]for i in range(M)if put[i]]) <= C:
                max1 = max((max1, sum([range1[i] ** 2 for i in range(M)if put[i]])))
    
    max2 = 0
    range2 = goods[y2][x2:(x2+M)]
    if sum(range2) <= C:
        max2 = sum([x**2 for x in range2])
    else:
        for put in put_list:
            if sum([range2[i] for i in range(M)if put[i]]) <= C:
                max2 = max((max2, sum([range2[i] ** 2 for i in range(M)if put[i]])))
    
    max_val = max((max_val, max1+max2))

print(max_val)