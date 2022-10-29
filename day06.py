f = open("input/day06.txt")
lines = [line.rstrip() for line in f.readlines()]
lines = list(zip(*lines[::-1]))

message1 = ''
message2 = ''

for line in lines:
    counter = {c: line.count(c) for c in set(line)}
    message1 += max(sorted(counter), key=counter.get)
    message2 += min(sorted(counter), key=counter.get)

part1 = message1
part2 = message2

print(f'part 1: {part1}')
print(f'part 2: {part2}')
