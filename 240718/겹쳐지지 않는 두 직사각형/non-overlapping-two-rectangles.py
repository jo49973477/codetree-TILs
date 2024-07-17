import sys
import copy

N, M = map(int, sys.stdin.readline().split()) # N줄 M행
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dots = []
for l in range(M):
    for r in range(l, M):
        for t in range(N):
            for b in range(t, N):
                dots.append((l, r, t, b))

ans = - sys.maxsize


for l,r,t,b in dots:
    dots2 = []
    
    for dot2 in dots:
        l2, r2, t2, b2 = dot2
        if (l2 > r or t2 > b):
            dots2.append(dot2)
    
    for dot2 in dots2:
        l2, r2, t2, b2 = dot2
        recsum1 = sum([sum(line[l:r+1]) for line in field[t:b+1]])
        recsum2 = sum([sum(line[l2:r2+1]) for line in field[t2:b2+1]])
        ans = max((ans, recsum1+recsum2 ))
        

print(ans)