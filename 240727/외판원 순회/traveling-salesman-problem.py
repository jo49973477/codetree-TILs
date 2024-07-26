import sys



N = int(sys.stdin.readline())
costs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

min_cost = sys.maxsize

def permu(depth, visited, arr):
    if depth == N:
        _from = arr[-1]
        cost = 0
        for _to in arr:
            cost += costs[_from][_to]
            _from = _to

        global min_cost
        min_cost = min((min_cost, cost))
        
    for i in range(N):
        if visited[i]:
            continue
        else:
            visited[i] = True
            arr[depth] = i
            permu(depth + 1, visited, arr)
            visited[i] = False

permu(0, [False for _ in range(N)], [0 for _ in range(N)])
print(min_cost)