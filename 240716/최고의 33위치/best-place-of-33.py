import sys

N = int(sys.stdin.readline())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


max = 0
for i in range(N-2):
    for j in range(N-2):
        val = sum([sum(line[j:(j+3)]) for line in field[i:(i+3)]])
        max = val if val >= max else max
        
print(max)