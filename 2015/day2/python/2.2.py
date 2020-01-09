import sys

with open('2.in') as file:
    lines = file.readlines()

total_footage = 0
total_ribbon = 0

for line in lines:
    x, y, z = [int(c) for c in line.rstrip().split('x')]
    areas = [x*y, x*z, y*z]
    perimeters = [2 * x + 2 * y, 2 * x + 2 * z, 2 * y + 2 * z]
    smallest_perimeter = min(perimeters)
    smallest_area = min(areas)
    total_ribbon += smallest_perimeter + x * y * z
    total_footage += 2 * sum(areas) + smallest_area

print(total_footage)
print(total_ribbon)
