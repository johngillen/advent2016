f = open("input/day02.txt")
lines = [line.rstrip() for line in f.readlines()]

keypad1 = [0, 0, 0, 0, 0], \
          [0, 1, 2, 3, 0], \
          [0, 4, 5, 6, 0], \
          [0, 7, 8, 9, 0], \
          [0, 0, 0, 0, 0]

keypad2 = [0, 0, 0, 0, 0, 0, 0], \
          [0, 0, 0, 1, 0, 0, 0], \
          [0, 0, 2, 3, 4, 0, 0], \
          [0, 5, 6, 7, 8, 9, 0], \
          [0, 0, 'A', 'B', 'C', 0, 0], \
          [0, 0, 0, 'D', 0, 0, 0], \
          [0, 0, 0, 0, 0, 0, 0]

def process(keypad):
    code = ''
    coords = []
    for i in range(len(keypad)):
        for j in range(len(keypad[i])):
            if keypad[i][j] == 5:
                coords = [i, j]
    for line in lines:
        for c in line:
            if c == 'U':
                coords[0] -= 1
                if keypad[coords[0]][coords[1]] == 0:
                    coords[0] += 1
            if c == 'D':
                coords[0] += 1
                if keypad[coords[0]][coords[1]] == 0:
                    coords[0] -= 1
            if c == 'L':
                coords[1] -= 1
                if keypad[coords[0]][coords[1]] == 0:
                    coords[1] += 1
            if c == 'R':
                coords[1] += 1
                if keypad[coords[0]][coords[1]] == 0:
                    coords[1] -= 1

        code += str(keypad[coords[0]][coords[1]])
    return code

part1 = process(keypad1)
part2 = process(keypad2)

print(f'part 1: {part1}')
print(f'part 2: {part2}')
