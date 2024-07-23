import sys

N, M, T, K = map(int, sys.stdin.readline().split())
marvels = [list(sys.stdin.readline().split()) for _ in range(M)]
marvels = [[int(r)-1, int(c)-1, d, int(v), i] for i, (r, c, d, v) in enumerate(marvels)]

def move(r, c, dir, v):#미1친 새끼들아 인간승리다 내가 이거 O(1)만에 해결할지 몰랐지?
    if dir == 'D':
        clps = (v+r) // (N-1)
        r = v+r if clps % 2 == 0 else -v-r+2*(N-1)*clps
        r %= (N-1)*2
        dir = 'D' if clps % 2 == 0 else 'U'
    elif dir == 'R':
        clps = (v+c) // (N-1)
        c = v+c if clps % 2 == 0 else -v-c+2*(N-1)*clps
        c %= (N-1)*2
        dir = 'R' if clps % 2 == 0 else 'L'
    elif dir == 'L':
        clps = (v-c+N-1) // (N-1)
        c = -v+c+2*(N-1)*clps if clps % 2 == 0 else v-c
        c %= (N-1)*2
        dir = 'L' if clps % 2 == 0 else 'R'
    elif dir == 'U':
        clps = (v-r+N-1) // (N-1)
        r = r-v+2*(N-1)*clps if clps % 2 == 0 else -r+v
        r %= (N-1)*2
        dir = 'U' if clps % 2 == 0 else 'D'
        
    return r, c, dir, v
        
count = [[0 for _ in range(N)] for _ in range(N)]
for r, c, _, _, _ in marvels:
    count[r][c] += 1

for _ in range(T):
    new_count = [[0 for _ in range(N)] for _ in range(N)]
    new_marvels = []
    
    for i, (r, c, d, v, num) in enumerate(marvels):
        new_r, new_c, new_d, new_v = move(r,c,d,v)
        marvels[i] = [new_r, new_c, new_d, new_v, num]
        new_count[new_r][new_c] += 1
    
    assholes_dic = {}
    
    for r, c, d, v, num in marvels:
        if new_count[r][c] == 1:
            new_marvels.append([r,c,d,v, num])
        elif new_count[r][c] > 1:
            if (r,c) in assholes_dic:
                assholes_dic[(r,c)].append([d,v, num])
            else:
                assholes_dic[(r,c)] = [[d,v, num]]
    
    for (r,c), asshole_list in assholes_dic.items():
        asshole_list.sort(key = lambda x : (x[1], x[2]), reverse=True)
        
        for d, v, num in asshole_list[:K]:
            new_marvels.append([r,c,d,v,num])
        
        new_count[r][c] = len(asshole_list[:K])
    
    count = new_count
    marvels = new_marvels
    

print(sum([sum(l) for l in count]))