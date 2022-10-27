import re

f = open("input/day04.txt")
lines = [line.rstrip() for line in f.readlines()]

sectorsum = 0
target = 0

for line in lines:
    name = re.search(r'(\w*-)*', line).group(0)[:-1]
    hash = re.search(r'\[(\w*)\]', line).group(0)[1:-1]
    sector = re.search(r'(\d+)', line).group(0)
    name = name.replace('-', '')
    sector = int(sector)

    counter = {c: name.count(c) for c in set(name)}
    namehash = ''
    for i in range(5):
        namehash += max(sorted(counter), key=counter.get)
        counter.pop(namehash[-1])

    if namehash == hash:
        sectorsum += sector
        name = ''.join([chr((ord(c) - ord('a') + sector) % 26 + ord('a')) for c in name])
        if 'northpoleobjectstorage' == name:
            target = sector

part1 = sectorsum
part2 = target

print(f'part 1: {part1}')
print(f'part 2: {part2}')
