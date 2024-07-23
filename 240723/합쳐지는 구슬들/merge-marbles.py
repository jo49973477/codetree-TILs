import sys

N, M, T = map(int, sys.stdin.readline().split())
marvels = [list(sys.stdin.readline().split()) for _ in range(M)]
marvels = [[int(r)-1, int(c)-1, d, int(w), idx] for idx, (r,c,d,w) in enumerate(marvels)]

dir_dic = {'U': (0, -1), 'D': (0, 1), 'R': (1, 0), 'L': (-1, 0)}
chdir_dic = {'U':'D', 'D':'U', 'R':'L', 'L':'R'}
    
for _ in range(T):
    
    for idx, (y, x, d, w, num) in enumerate(marvels):
        dx, dy = dir_dic[d]
        
        if 0 <= x+dx <= N-1 and 0 <= y+dy <= N-1:
            y, x = y+dy, x+dx
        else:
            d = chdir_dic[d]
            
        marvels[idx] = [y, x, d, w, num]
    
    count_dic = {}    
    for y, x, _, _, _ in marvels:
        if (y, x) in count_dic:
            count_dic[(y,x)] += 1
        else:
            count_dic[(y,x)] = 1
    
    new_marvels = []
    assholes_dic = {}
    
    for y, x, d, w, num in marvels:
        if count_dic[(y,x)] == 1:
            new_marvels.append([y,x,d,w,num])
        elif count_dic[(y,x)] > 1:
            if (y,x) in assholes_dic:
                assholes_dic[(y,x)].append([d,w,num])
            else:
                assholes_dic[(y,x)] = [[d,w,num]]
                
    for (y,x), asshole_list in assholes_dic.items():
        asshole_list.sort(key = lambda x : (x[2]), reverse=True)
        d, _ , num = asshole_list[0]
        w = sum([x[1] for x in asshole_list])
        new_marvels.append([y,x,d,w,num])
        
    marvels = new_marvels

print(len(marvels), max(x[3] for x in marvels))