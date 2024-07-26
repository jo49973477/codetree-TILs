import sys



N = int(sys.stdin.readline())
field = [sys.stdin.readline() for _ in range(N)]

coins_arr = []
pos_dic = {}
for i in range(N):
    for j in range(N):
        if field[i][j] == 'S' or field[i][j] == 'E':
            pos_dic[field[i][j]] = (i, j)
        elif field[i][j] == '.':
            continue
        else:
            pos_dic[int(field[i][j])] = (i, j)
            coins_arr.append(int(field[i][j]))
            
coins_arr.sort()


min_dist = sys.maxsize

def choose(depth, result, last_idx):
    
    if depth == 3:
        route = [pos_dic[coin] for coin in result] + [pos_dic['E']]
    
        dist = 0
        now_y, now_x = pos_dic['S']
        for y, x in route:
            dist += abs(y-now_y) + abs(x-now_x)
            now_y, now_x = y, x
        global min_dist
        min_dist = min((min_dist, dist))
            
    else:
        for idx in range(last_idx + 1, len(coins_arr)):
            result[depth] = coins_arr[idx]
            choose(depth + 1, result, idx)

choose(0, [0,0,0] ,-1)
print(min_dist if min_dist != sys.maxsize else -1)