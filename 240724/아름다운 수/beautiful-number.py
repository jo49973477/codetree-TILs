import sys

N = int(sys.stdin.readline())

ans = 0

def backtrack(put_len, result):
    if len(result) == N:
        global ans
        ans += 1
    else:
        for num in range(1, put_len+1):
            new_result = result + (str(num) * num)
            backtrack(put_len - num, new_result)


backtrack(N, "")

print(ans)