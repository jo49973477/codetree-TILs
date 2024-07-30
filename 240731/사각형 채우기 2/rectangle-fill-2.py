import sys

N = int(sys.stdin.readline())
block_dic = {1:1, 2: 3}

def nums(n):
    global block_dic
    
    if n in block_dic:
        return block_dic[n]
    else:
        val = (nums(n-1)  + nums(n-2) * 2) % 10_007
        block_dic[n] = val
        return val

print(nums(N))