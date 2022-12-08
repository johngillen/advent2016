f = open("input/day07.txt")
lines = [line.rstrip() for line in f.readlines()]

from re import split

def abba(s):
    s = [s[i:i + 4] for i in range(len(s) - 3)]
    for g in s:
        if (g[:2] == g[::-1][:2]) and (g[0] != g[1]):
            return True
    return False

def aba(s):
    l = []
    s = [s[i:i + 3] for i in range(len(s) - 2)]
    for g in s:
        if (g[:2] == g[::-1][:2]) and (g[0] != g[1]):
            l += [str(g[1:] + g[1])]
    return l

part1 = 0
part2 = 0

for line in lines:
    line = split(r'\[|\]', line)

    outside = line[::2]
    inside = line[1::2]

    tls = False
    for s in outside:
        if abba(s):
            tls = True
            break
    for s in inside:
        if abba(s):
            tls = False
            break
            
    ssl = False
    twins = [] 
    [twins.extend(aba(s)) for s in outside]
    for s in inside:
        for t in twins:
            if t in s:
                ssl = True
                break
    part1 += 1 if tls else 0
    part2 += 1 if ssl else 0

print(f'part 1: {part1}')
print(f'part 2: {part2}')
