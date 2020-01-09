import sys
from itertools import permutations

def readNumbers(filename):
    with open(filename) as file:
        return file.read().split(',')

def parse_opcode(c):
    num = str(c).zfill(5);
    code = int(num[-2:])
    first_mode = int(num[2])
    second_mode = int(num[1])
    third_mode = int(num[0])
    return {'code': code, 'first': first_mode, 'second': second_mode, 'third': third_mode}

def run_program(orig_numbers, phase_setting, input_signal):
    numbers = orig_numbers.copy()
    current_index = 0
    in_count = 0
    running = True
    while running:
        current_code = parse_opcode(numbers[current_index])
        if current_code['code'] in [1, 2, 7, 8]:
            val1 = numbers[current_index + 1] if current_code['first'] == 1 else numbers[numbers[current_index + 1]]
            val2 = numbers[current_index + 2] if current_code['second'] == 1 else numbers[numbers[current_index + 2]]
            result_index = numbers[numbers[current_index + 3]] if current_code['third'] == 1 else numbers[current_index + 3]
            current_index += 4
        if current_code['code'] == 1:
            result = val1 + val2
        elif current_code['code'] == 2:
            result = val1 * val2
        elif current_code['code'] == 3:
            if in_count == 0:
                result = phase_setting
            elif in_count == 1:
                result = input_signal
            else:
                result = int(input('Enter System ID: '))
            result_index = numbers[current_index + 1]
            in_count += 1
            current_index += 2
        elif current_code['code'] == 4:
            result = numbers[current_index + 1] if current_code['first'] == 1 else numbers[numbers[current_index + 1]]
            current_index +=  2
            return(result)
        elif current_code['code'] == 5:
            val1 = numbers[current_index + 1] if current_code['first'] == 1 else numbers[numbers[current_index + 1]]
            if val1 != 0:
                current_index = numbers[current_index + 2] if current_code['second'] == 1 else numbers[numbers[current_index + 2]]
            else:
                current_index += 3
        elif current_code['code'] == 6:
            val1 = numbers[current_index + 1] if current_code['first'] == 1 else numbers[numbers[current_index + 1]]
            if val1 == 0:
                current_index = numbers[current_index + 2] if current_code['second'] == 1 else numbers[numbers[current_index + 2]]
            else:
                current_index += 3
        elif current_code['code'] == 7:
            numbers[result_index] = 1  if val1 < val2 else 0
        elif current_code['code'] == 8:
            numbers[result_index] =  1 if val1 == val2 else 0
        elif current_code['code'] == 99:
            sys.exit(1)
        else:
            print("An Error Occured")
            sys.exit(0)

        if current_code['code'] in [1, 2, 3]:
            numbers[result_index] = result

original_numbers = list(map(int, readNumbers('7.in')))
phases = [0, 1, 2, 3, 4]
max_signal = 0
for phase_code in list(permutations(phases)):
	signal = 0
	for phase in phase_code:
		signal = run_program(original_numbers, phase, signal)
	if signal > max_signal:
		max_signal = signal

print(max_signal)
# run_program(original_numbers)

# TODO
#
# run_program should run now, and return the value expected instead of printing the output from an opcode
# of 4
#
# still need to work through and loop through the other input [0, 1, 2, 3, 4] once each in every combination,
# and flow results through to the next ampifier program run.
# 
 
