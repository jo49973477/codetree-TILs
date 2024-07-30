import sys
from collections import deque

N = int(sys.stdin.readline())

q = deque()
q.append((N, 0))

ans = 0
already = set()

while q:
    num, times = q.popleft()
    
    if num == 1:
        ans = times
        break
    
    arr = [num - 1, num + 1]
    if num % 2 == 0:
        arr.append(num//2)
    if num % 3 == 0:
        arr.append(num//3)
    
    for asshole in arr:
        if asshole not in already:
            q.append((asshole, times+1))
            already.add(asshole)
        
print(ans)