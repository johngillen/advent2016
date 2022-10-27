f = open("input/day01.txt")
lines = [line.rstrip() for line in f.readlines()]

visited = [(0, 0)]

for line in lines:
    x = 0
    y = 0
    a = 270
    for direction in line.split(', '):
        turn = direction[0]
        move = int(direction[1::])
        a += -90 if turn == 'L' else 90
        if a == -90:
            a = 270
        if a == 360:
            a = 0

        for i in range(move):
            if a == 0:
                x += 1
            if a == 90:
                y -= 1
            if a == 180:
                x -= 1
            if a == 270:
                y += 1
            visited.append((x, y))

part1 = x + y
part2 = 0

seen = []
for i in visited:
    if i in seen:
        part2 = sum(i)
        break
    seen.append(i)


print(f'part 1: {part1}')
print(f'part 2: {part2}')
