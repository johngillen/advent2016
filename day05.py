from hashlib import md5

f = open("input/day05.txt")
lines = [line.rstrip() for line in f.readlines()]
input = lines[0]

door1 = ''
door2 = [None]*8
i = 0
while None in door2:
    hex = md5((input + str(i)).encode()).hexdigest()
    if hex[:5] == '00000':
        door1 += hex[5]
        try:
            if door2[int(hex[5])] is None:
                door2[int(hex[5])] = hex[6]
        except:
            pass
    i += 1

part1 = door1[:8]
part2 = ''.join(door2)

print(f'part 1: {part1}')
print(f'part 2: {part2}')
