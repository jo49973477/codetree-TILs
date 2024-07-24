import sys

st = sys.stdin.readline().strip() # c-a*b
variables = []
for i in range(len(st)//2 + 1):
    if st[2*i] not in variables:
        variables.append(st[2*i])

M = len(variables)

ans = 0

def backtrack(depth, l):
    if depth == M:
        
        var_dic = {variables[i] : l[i] for i in range(M)}
        result = var_dic[st[0]]
        for i in range(1, len(st), 2):
            if st[i] == '+':
                result += var_dic[st[i+1]]
            elif st[i] == '-':
                result -= var_dic[st[i+1]]
            elif st[i] == '*':
                result *= var_dic[st[i+1]]
        
        global ans
        ans = max((ans, result))
        
    else:
        for num in range(1, 5):
            l[depth] = num
            backtrack(depth+1, l)


vals = [0 for _ in range(M)]
backtrack(0, vals)
print(ans)