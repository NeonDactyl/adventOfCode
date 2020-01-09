class Claim:
    def __init__(self, id, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.id = id

claims = []
fabric = {}

with open("input") as file:
    for line in file:
        id, _, coord, size = line.split()
        id = id[1:]
        coord = coord[:-1].split(',')
        size = size.split('x')
        claims.append(Claim(int(id), int(coord[0]), int(coord[1]), int(size[0]), int(size[1])))

for claim in claims:
    for i in range(claim.width):
        for j in range(claim.height):
            fabric[(claim.x + i, claim.y + j)] = fabric.get((claim.x + i, claim.y + j), 0) + 1

for claim in claims:
    overlaps = False
    for i in range(claim.width):
        for j in range(claim.height):
            if fabric[(claim.x + i, claim.y + j)] > 1: overlaps = True
    if not overlaps:
        print(claim.id)
