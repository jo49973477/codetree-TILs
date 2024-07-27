from collections import deque
import sys

N = int(sys.stdin.readline())
q = deque()

for _ in range(N):
    order = sys.stdin.readline().split()
    
    if order[0] == 'push':
        num = int(order[1])
        q.append(num)
    elif order[0] == 'front':
        print(q[0])
    elif order[0] == 'pop':
        print(q.popleft())
    
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        print(0 if q else 1)