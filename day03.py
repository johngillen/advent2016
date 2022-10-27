f = open("input/day03.txt")
lines = [line.rstrip() for line in f.readlines()]

valid = 0
for line in lines:
    line = [int(n) for n in line.split()]
    line.sort()
    if sum(line[0:2]) > line[2]:
        valid += 1

buffer = []
valid = 0
validvert = 0
for line in lines:
    line = [int(n) for n in line.split()]
    buffer.append(line.copy())

    line.sort()
    if sum(line[0:2]) > line[2]:
        valid += 1
    
    if len(buffer) == 3:
        for j in range(len(buffer[0])):
            comp = [buffer[0][j], buffer[1][j], buffer[2][j]]
            comp.sort()
            if sum(comp[0:2]) > comp[2]:
                validvert += 1
        buffer = []

part1 = valid
part2 = validvert

print(f'part 1: {part1}')
print(f'part 2: {part2}')
