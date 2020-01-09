import difflib
import sys

items = []
twos = 0
threes = 0
with open("input") as f:
    for line in f:
        items.append(str(line.strip()))

for idx, id in enumerate(items):
    for compare_with in items[idx+1:]:

        c = 0
        for i, s in enumerate(difflib.ndiff(id, compare_with)):
            if s[0] == ' ': continue
            else: c += 1
        if  c == 2:
            print("first:  ", id)
            print("second: ", compare_with)
            sys.exit(0)
