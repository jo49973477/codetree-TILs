import sys
limit_number = 1000000
sys.setrecursionlimit(limit_number)


def makearray(sen, N, startpoint):
    if len(sen) == N:
        print(sen)
        return
    
    max_conlen = len(sen) // 2 if len(sen)%2 == 0 else len(sen) // 2 + 1
    next_candidates = list(range(startpoint, 7))
        
    for conlen in range(1, max_conlen + 1):
        if not next_candidates:
            break
        else:
            for can in next_candidates:
                last1 = sen[(len(sen)-conlen+1):]
                last2 = sen[(len(sen)-2*conlen+1):(len(sen)-conlen+1)]
                if last1 + str(can) == last2:
                    next_candidates.remove(can)
    
    if next_candidates:
        makearray(sen+str(next_candidates[0]), N, 4)
    else:
        makearray(sen[:-1], N, startpoint + 1)
            
N = int(sys.stdin.readline())
makearray('4', N, 4)