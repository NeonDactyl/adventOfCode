x, y = 0, 0

with open("3.in") as file:
    instructions = file.read().rstrip()

positions = {(0, 0): 1}
multiples = {}

for i in instructions:
    if i == '^':
        y += 1
    elif i == '>':
        x += 1
    elif i == 'v':
        y -= 1
    elif i == '<':
        x -= 1
    else:
        print("This should not happen... Exiting")
        sys.exit()
    positions[(x, y)] = positions.get((x, y), 0) + 1
    if positions[(x, y)] > 1:
        multiples[(x, y)] = True
print(len(multiples))
