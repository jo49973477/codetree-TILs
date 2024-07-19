import sys

N, M = map(int, sys.stdin.readline().split())
bombs = [int(sys.stdin.readline()) for _ in range(N)]

isExplode = True
while isExplode:
    isExplode = False
    repeat = 1
    for i in range(len(bombs)):
        if i == len(bombs)-1 or bombs[i] != bombs[i+1]:
            if repeat >= M:
                isExplode = True
                for j in range(repeat):
                    bombs[i-j] = 0
            repeat = 1
        elif bombs[i] == bombs[i+1]:
            repeat += 1
    
    new_bombs = []
    for bomb in bombs:
        if bomb != 0:
            new_bombs.append(bomb)
    
    bombs = new_bombs
    

print(len(bombs))
print('\n'.join(map(str, bombs)))