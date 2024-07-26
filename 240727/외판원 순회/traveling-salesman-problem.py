import sys
import copy



N = int(sys.stdin.readline())
costs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

min_cost = sys.maxsize

def permu(depth, visited, arr):
    if depth == N-1:
        arr.append(0)
        _from = arr[-1]
        cost = 0
        for _to in arr:
            if costs[_from][_to] == 0:
                cost = -1
                break
            else:
                cost += costs[_from][_to]
                _from = _to
        arr.pop()

        if cost != -1:
            global min_cost
            min_cost = min((min_cost, cost))
        
    for i in range(N-1):
        if visited[i]:
            continue
        else:
            visited[i] = True
            arr[depth] = i+1
            permu(depth + 1, visited, arr)
            visited[i] = False

permu(0, [False for _ in range(N-1)], [0 for _ in range(N-1)])
print(min_cost)