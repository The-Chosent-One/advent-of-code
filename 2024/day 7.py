import re
from math import log10

with open("input.txt", "r") as file:
    inp = [re.findall(r"\d+", line) for line in file.read().split("\n")]
    cases = [[*map(int, line)] for line in inp]

def is_possible(operands: list[int], operand_index: int, final_value: int, part2: bool = False) -> bool:
    if operand_index == 0:
        return final_value == operands[0]

    last_operand = operands[operand_index]
    vals = []

    if final_value % last_operand == 0:
        vals.append(final_value // last_operand)
    
    if part2:
        num_of_digits = int(log10(last_operand)) + 1
        quotient, remainder = divmod(final_value, 10 ** num_of_digits)
        if remainder == last_operand:
            vals.append(quotient)
    
    vals.append(final_value - last_operand)

    return any(is_possible(operands, operand_index - 1, v, part2=part2) for v in vals)

part1 = part2 = 0
for final_value, *operands in cases:
    if is_possible(operands, len(operands) - 1, final_value):
        part1 += final_value
        part2 += final_value
        continue
    
    if is_possible(operands, len(operands) - 1, final_value, part2=True):
        part2 += final_value

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

