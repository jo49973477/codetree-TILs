import sys

N = int(sys.stdin.readline())
zenga = [int(sys.stdin.readline()) for _ in range(N)]
s1, e1 = map(int, sys.stdin.readline().split())
s2, e2 = map(int, sys.stdin.readline().split())

s1, e1 = s1-1, e1-1
zenga = zenga[:s1] + zenga[(e1+1):]

s2, e2 = s2-1, e2-1
zenga = zenga[:s2] + zenga[(e2+1):]

print(len(zenga))
print('\n'.join(map(str, zenga)))