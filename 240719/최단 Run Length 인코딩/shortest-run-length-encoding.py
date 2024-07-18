import sys

sen = sys.stdin.readline().strip()

ans = sys.maxsize
for i in range(len(sen)):
    sen = sen[-1] + sen[:-1]
    
    start = 0
    shortend = ''
    for i in range(len(sen)):
        if i == len(sen)-1 or sen[i] != sen[i+1]:
            shortend += sen[i] + str(i+1-start)
            start = i+1
    ans = min((ans, len(shortend)))

print(ans)