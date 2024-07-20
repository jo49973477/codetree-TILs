import sys

field = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]
dir = sys.stdin.readline().strip()

grav_field = [[0 for _ in range(4)] for _ in range(4)]

if dir == 'L':
    for row in range(4):
        last = 0
        for col in range(4):
            if field[row][col] == 0:
                continue
            else:
                grav_field[row][last] = field[row][col]
                last += 1
elif dir == 'R':
    for row in range(4):
        last = 3
        for col in range(3, -1, -1):
            if field[row][col] == 0:
                continue
            else:
                grav_field[row][last] = field[row][col]
                last -= 1
elif dir == 'U':
    for col in range(4):
        last = 0
        for row in range(4):
            if field[row][col] == 0:
                continue
            else:
                grav_field[last][col] = field[row][col]
                last += 1
elif dir == 'D':
    for col in range(4):
        last = 3
        for row in range(3, -1, -1):
            if field[row][col] == 0:
                continue
            else:
                grav_field[last][col] = field[row][col]
                last -= 1


field = grav_field

new_field = [[0 for _ in range(4)] for _ in range(4)]

if dir == 'L':
    for row in range(4):
        last = 0
        repeat = 1
        for col in range(4):
            if field[row][col] == 0:
                continue
            elif col == 3 or field[row][col] != field[row][col + 1]:
                if repeat == 1:
                    new_field[row][last] = field[row][col]
                    last += 1
                elif repeat == 2:
                    new_field[row][last] = field[row][col] * 2
                    last += 1
                elif repeat == 3:
                    new_field[row][last] = field[row][col] * 2
                    new_field[row][last + 1] = field[row][col]
                    last += 2
                elif repeat == 4:
                    new_field[row][last] = field[row][col] * 2
                    new_field[row][last + 1] = field[row][col] * 2
                    last += 2
                repeat = 1
            elif field[row][col] == field[row][col + 1]:
                repeat += 1
elif dir == 'R':
    for row in range(4):
        last = 3
        repeat = 1
        for col in range(3, -1, -1):
            if field[row][col] == 0:
                continue
            elif col == 0 or field[row][col] != field[row][col-1]:
                if repeat == 1:
                    new_field[row][last] = field[row][col]
                    last -= 1
                elif repeat == 2:
                    new_field[row][last] = field[row][col] * 2
                    last -= 1
                elif repeat == 3:
                    new_field[row][last] = field[row][col] * 2
                    new_field[row][last-1] = field[row][col]
                    last -= 2
                elif repeat == 4:
                    new_field[row][last] = field[row][col] * 2
                    new_field[row][last-1] = field[row][col] * 2
                    last -= 2
                repeat = 1
            elif field[row][col] == field[row][col-1]:
                repeat += 1
elif dir == 'U':
    for col in range(4):
        last = 0
        repeat = 1
        for row in range(4):
            if field[row][col] == 0:
                continue
            elif row == 3 or field[row][col] != field[row+1][col]:
                if repeat == 1:
                    new_field[last][col] = field[row][col]
                    last += 1
                elif repeat == 2:
                    new_field[last][col] = field[row][col] * 2
                    last += 1
                elif repeat == 3:
                    new_field[last][col] = field[row][col] * 2
                    new_field[last+1][col] = field[row][col]
                    last += 2
                elif repeat == 4:
                    new_field[last][col] = field[row][col] * 2
                    new_field[last+1][col] = field[row][col] * 2
                    last += 2
                repeat = 1
            elif field[row][col] == field[row+1][col]:
                repeat += 1
elif dir == 'D':
    for col in range(4):
        last = 3
        repeat = 1
        for row in range(3, -1, -1):
            if field[row][col] == 0:
                continue
            elif row == 0 or field[row][col] != field[row-1][col]:
                if repeat == 1:
                    new_field[last][col] = field[row][col]
                    last -= 1
                elif repeat == 2:
                    new_field[last][col] = field[row][col] * 2
                    last -= 1
                elif repeat == 3:
                    new_field[last][col] = field[row][col] * 2
                    new_field[last-1][col] = field[row][col]
                    last -= 2
                elif repeat == 4:
                    new_field[last][col] = field[row][col] * 2
                    new_field[last-1][col] = field[row][col] * 2
                    last -= 2
                repeat = 1
            elif field[row][col] == field[row-1][col]:
                repeat += 1


print('\n'.join([' '.join(map(str, line)) for line in new_field]))