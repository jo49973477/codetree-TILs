import sys

N, M = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


lines = field + [[field[i][j] for i in range(N)] for j in range(N)]

ans = 0
for line in lines:
    line_repeat = 1
    repeat = 1
    
    for i in range(len(line)-1):
        repeat = repeat + 1 if line[i] == line[i+1] else 1
        line_repeat = max((repeat, line_repeat))
    
    ans = ans + 1 if line_repeat >= M else ans
    
print(ans)