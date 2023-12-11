import re

with open("input.txt") as file:
    inp = file.read()

# part 1
part1 = 0

for match in zip(re.findall(r"\b\D*(\d)", inp), re.findall(r"(\d)\D*\b", inp)):
    part1 += int("".join(match))

print(part1)

# part 2
part2 = 0
mapping = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
lines = inp.split()


for line in lines:
    start_ptr = end_ptr = 0
    digits = []

    while end_ptr != len(line) + 1:
        current = line[start_ptr: end_ptr]
        latest = current[-1] if current else ""

        if latest.isdigit():
            digits.append(int(latest))
            start_ptr = end_ptr
            end_ptr = start_ptr + 1
            continue

        for replace, replacement in mapping.items():
            if replace in current:
                digits.append(replacement)
                start_ptr = end_ptr = end_ptr - 1 # includes the last letter of whatever we matched
        
        end_ptr += 1
    
    part2 += digits[0] * 10 + digits[-1]

print(part2)
