def getCodes(line):
    return map(lambda x: (x[0], int(x[1:])),line.split(','))

with open('input') as file:
    wire1 = getCodes(file.readline())
    wire2 = getCodes(file.readline())

intersections = []
grid = {}

position = [0,0]
steps = 0
for code in wire1:
    for i in range(code[1]):
        steps += 1
        if code[0] == 'R':
            position[0] += 1
        elif code[0] == 'D':
            position[1] -= 1
        elif code[0] == 'L':
            position[0] -= 1
        else:
            position[1] += 1
        grid[tuple(position)] = min([steps, grid.get(tuple(position), steps+1)])

position = [0,0]
steps = 0
for code in wire2:
    for i in range(code[1]):
        steps += 1
        if code[0] == 'R':
            position[0] += 1
        elif code[0] == 'D':
            position[1] -= 1
        elif code[0] == 'L':
            position[0] -= 1
        else:
            position[1] += 1
        if grid.get(tuple(position), 0) != 0:
            intersections.append(grid[tuple(position)] + steps)

print(min(intersections))
