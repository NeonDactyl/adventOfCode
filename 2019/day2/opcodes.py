import sys

def readNumbers(filename):
    with open(filename) as file:
        return file.read().split(',')

def run_program(numbers):
    for idx, number in enumerate(numbers):
        if idx % 4 == 0 and number == 99:
            break

        if idx % 4 != 0:
            continue
        new_idx = numbers[idx+3]
        a = numbers[numbers[idx+1]]
        b = numbers[numbers[idx+2]]
        result = 0
        if number == 1:
            result = a + b
            numbers[new_idx] = result
        if number == 2:
            result = a * b
            numbers[new_idx] = result
    return numbers[0]

original_numbers = list(map(int, readNumbers('input')))

for a in range(100):
    for b in range(100):
        numbers = original_numbers.copy()
        numbers[1] = a
        numbers[2] = b
        if (run_program(numbers) == 19690720):
            print("{}  {}".format(a, b))
            sys.exit()
