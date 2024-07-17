import sys

N, T = map(int, sys.stdin.readline().split()) # N줄 M행
belt1 = list(map(int, sys.stdin.readline().split()))
belt2 = list(map(int, sys.stdin.readline().split()))
belt3 = list(map(int, sys.stdin.readline().split()))

for _ in range(T):
    b1, b2, b3 = belt1[:], belt2[:], belt3[:]
    belt1 = [b3[-1]] + b1[:-1]
    belt2 = [b1[-1]] + b2[:-1]
    belt3 = [b2[-1]] + b3[:-1]

print(' '.join(map(str, belt1)))
print(' '.join(map(str, belt2)))
print(' '.join(map(str, belt3)))