import sys

ans = 0

def backtrack(lines, line_num, last):
    global ans
    
    if not lines:
        ans = max((ans, line_num))
    else:
        isObservable = False
        for i, (x1, x2) in enumerate(lines):
            if x1 > last:
                isObservable = True
                backtrack(lines[(i+1):], line_num + 1, x2)
            else:
                continue
        if not isObservable:
            ans = max((ans, line_num))            

N = int(sys.stdin.readline())
lines = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
lines.sort(key= lambda x: x[0])

backtrack(lines, 0, 0)
print(ans)