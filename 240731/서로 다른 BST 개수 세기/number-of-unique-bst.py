import sys

N = int(sys.stdin.readline())
tree_dic = {0:1, 1:1, 2:2,}

def nums(n):
    global tree_dic
    
    if n in tree_dic:
        return tree_dic[n]
    else:
        val = sum([nums(i) * nums(n-1-i) for i in range(1, n-1)]) + 2* nums(n-1)
        tree_dic[n] = val
        return val

print(nums(N))