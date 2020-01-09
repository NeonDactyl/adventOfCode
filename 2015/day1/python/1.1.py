import sys

filename = "1.in"

with open(filename) as f:
    instructions = f.read().strip()

current_floor = 0

for i, c in enumerate(instructions):
    if c == '(':
        current_floor += 1
    elif  c == ')':
        current_floor -= 1
    else:
        print("Um... this shouldn't happen with proper input.")
        sys.exit()
    if current_floor < 0:
        print(f'Stopped at {i}')
        sys.exit()

print(current_floor)
