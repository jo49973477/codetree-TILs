import sys

N = int(sys.stdin.readline())
block_dic = {1: 1, 2:2, }

def climb(n):
    global block_dic
    
    if n in block_dic:
        return block_dic[n]
    else:
        val = (climb(n-1) + climb(n-2)) % 10007
        block_dic[n] = val
        return val

print(climb(N))