import sys
from itertools import permutations


def readNumbers(filename):
    with open(filename) as file:
        return file.read().split(',')

class Amplifier:
	def __init__(self, numbers, phase):
		self.numbers = numbers.copy()
		self.phase = phase
		self.current_index = 0
		self.phase_used = False

	def parse_opcode(self, c):
		num = str(c).zfill(5);
		code = int(num[-2:])
		first_mode = int(num[2])
		second_mode = int(num[1])
		third_mode = int(num[0])
		return {'code': code, 'first': first_mode, 'second': second_mode, 'third': third_mode}

	def run_program(self, input_signal):
		running = True
		while running:
			current_code = self.parse_opcode(self.numbers[self.current_index])
			if current_code['code'] in [1, 2, 7, 8]:
				val1 = self.numbers[self.current_index + 1] if current_code['first'] == 1 else self.numbers[self.numbers[self.current_index + 1]]
				val2 = self.numbers[self.current_index + 2] if current_code['second'] == 1 else self.numbers[self.numbers[self.current_index + 2]]
				result_index = self.numbers[self.numbers[self.current_index + 3]] if current_code['third'] == 1 else self.numbers[self.current_index + 3]
				self.current_index += 4
			if current_code['code'] == 1:
				result = val1 + val2
			elif current_code['code'] == 2:
				result = val1 * val2
			elif current_code['code'] == 3:
				if not self.phase_used:
					result = self.phase
					self.phase_used = True
				else:
					result = input_signal
				result_index = self.numbers[self.current_index + 1]
				self.current_index += 2
			elif current_code['code'] == 4:
				result = self.numbers[self.current_index + 1] if current_code['first'] == 1 else self.numbers[self.numbers[self.current_index + 1]]
				self.current_index +=  2
				self.last_output = result
				# print("Code 4, returning: {}\nMoving to next Amp".format(result))
				return('4', result)
			elif current_code['code'] == 5:
				val1 = self.numbers[self.current_index + 1] if current_code['first'] == 1 else self.numbers[self.numbers[self.current_index + 1]]
				if val1 != 0:
					self.current_index = self.numbers[self.current_index + 2] if current_code['second'] == 1 else self.numbers[self.numbers[self.current_index + 2]]
				else:
					self.current_index += 3
			elif current_code['code'] == 6:
				val1 = self.numbers[self.current_index + 1] if current_code['first'] == 1 else self.numbers[self.numbers[self.current_index + 1]]
				if val1 == 0:
					self.current_index = self.numbers[self.current_index + 2] if current_code['second'] == 1 else self.numbers[self.numbers[self.current_index + 2]]
				else:
					self.current_index += 3
			elif current_code['code'] == 7:
				self.numbers[result_index] = 1  if val1 < val2 else 0
			elif current_code['code'] == 8:
				self.numbers[result_index] =  1 if val1 == val2 else 0
			elif current_code['code'] == 99:
				# print("Caught Code 99, returning value: ", end="")
				# print(self.last_output)
				return(('99', self.last_output))
			else:
				print("An Error Occured")
				sys.exit(0)

			if current_code['code'] in [1, 2, 3]:
				self.numbers[result_index] = result
			if self.current_index >= len(self.numbers):
				self.current_index = 0

original_numbers = list(map(int, readNumbers('7.in')))
phases = [5, 6, 7, 8, 9]
max_signal = 0
for phase_code in list(permutations(phases)):
	amps = []
	for i in phase_code:
		amps.append(Amplifier(original_numbers, i))
	running = True
	amp_index = 0
	signal = (0, 0)
	while running:
		signal = amps[amp_index].run_program(signal[1])
		if signal[0] == '99':
			running = False
			s = signal[1]
			if last_signal > max_signal:
				max_signal = last_signal
		elif signal[0] == '4':
			if amp_index == 4:
				last_signal =  signal[1]
			amp_index = (amp_index + 1) % len(amps)
		else:
			print("SYSTEM ERROR\n{}".format("#" * 80))
			sys.exit(1)
			

print(max_signal)
