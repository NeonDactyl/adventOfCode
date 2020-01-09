import sys

with open('2.in') as file:
    lines = file.readlines()

total_footage = 0

for line in lines:
    x, y, z = [int(c) for c in line.rstrip().split('x')]
    areas = [x*y, x*z, y*z]
    smallest = min(areas)
    total_footage += 2 * sum(areas) + smallest

print(total_footage)
