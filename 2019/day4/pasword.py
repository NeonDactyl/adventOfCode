def always_increasing(num):
    digits = str(num)
    for idx, digit in enumerate(digits):
        if idx == 0:
            continue
        if digit < digits[idx-1]:
            return False
    return True
    
def has_exactly_one_double_digit(num):
    digits = str(num)
    sequence = 1
    for x in range(1, 6):
        if digits[x] == digits[x-1]:
            sequence += 1
        elif sequence == 2:
            break
        else:
            sequence = 1
    if sequence == 2:
        return True

min = 172851
max = 675869
count = 0
for i in range(min, max):
    if always_increasing(i) and has_exactly_one_double_digit(i):
        count += 1

print(count)
