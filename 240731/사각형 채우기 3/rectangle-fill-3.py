import sys

N = int(sys.stdin.readline())
block_dic = {1:2, 2:7, 3:22}

def nums(n):
    global block_dic
    
    if n in block_dic:
        return block_dic[n]
    else:
        val = (sum([nums(i) for i in range(1, n)])*2 + 2 + nums(n-2))  % 1000_000_007
        block_dic[n] = val
        return val

print(nums(N))