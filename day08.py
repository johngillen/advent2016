f = open('input/day08.txt')
lines = [line.rstrip() for line in f.readlines()]

from re import findall

screen = [[' ' for _ in range(50)] for _ in range(6)]

for line in lines:
    a, b = map(int, findall(r'-?\d+', line))
    if 'rect' in line:
        for x, y in [(x, y) for x in range(b) for y in range(a)]:
            screen[x][y] = '█'
    elif 'rotate row' in line:
        screen[a] = screen[a][-b:] + screen[a][:-b]
    elif 'rotate column' in line:
        col = [screen[x][a] for x in range(len(screen))]
        col = col[-b:] + col[:-b]
        for x in range(len(screen)):
            screen[x][a] = col[x]

part1 = sum(row.count('█') for row in screen)

print(f'part 1: {part1}')
print(f'part 2: ')
[print(''.join(r)) for r in screen]
