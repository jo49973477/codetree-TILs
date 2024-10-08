import sys

N = int(sys.stdin.readline())
leg_list = list(map(int, sys.stdin.readline().split()))

ans = sys.maxsize
isMoved = False
def backtrack(pos, moved):
    if pos >= N-1:
        global ans
        ans = min((ans, moved))

        global isMoved
        isMoved = True
    else:
        for mv in range(1, leg_list[pos]+1):
            backtrack(pos + mv, moved + 1)

backtrack(0, 0)
print(ans if isMoved else -1)