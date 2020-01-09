from math import floor

total = 0

def calc_fuel(mass):
    if (mass < 9):
        return 0
    fuel = floor(mass / 3) - 2
    return fuel + calc_fuel(fuel)

with open("input") as file:
    for line in file:
        total += calc_fuel(int(line))

print(total)
