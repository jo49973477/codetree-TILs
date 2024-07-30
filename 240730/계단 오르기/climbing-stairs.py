import sys

N = int(sys.stdin.readline())
climb_dic = {1: 0, 2:1, 3:1, }

def climb(n):
    global climb_dic
    
    if n in climb_dic:
        return climb_dic[n]
    else:
        val = (climb(n-2) + climb(n-3)) % 10007
        climb_dic[n] = val
        return val

print(climb(N))