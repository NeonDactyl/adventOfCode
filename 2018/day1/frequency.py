import sys

shifts = []
freq = 0
past_freqs = []
shifts_idx = 0

with open("input") as f:
    for line in f:
        shifts.append(line)

while freq not in past_freqs:
    shift = shifts[shifts_idx]
    past_freqs.append(freq)

    if (shift[:1] == '-'):
        freq -= int(shift[1:])
    else:
        freq += int(shift[1:])
    shifts_idx = (shifts_idx + 1) % len(shifts)

    if (freq in past_freqs):
        print(freq)


print(len(past_freqs))
print(freq)
