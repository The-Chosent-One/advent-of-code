import re

with open("input.txt", "r") as file:
    A, B, C, *program = [*map(int, re.findall("\d+", file.read()))]

def get_combo_operand_value(operand: int, A: int, B: int, C: int) -> int:
    return [0, 1, 2, 3, A, B, C][operand]

def get_output(A: int, B: int, C: int) -> str:
    instruction_ptr = 0
    out = []

    while instruction_ptr < len(program):
        opcode, operand = program[instruction_ptr], program[instruction_ptr + 1]

        if opcode == 0:
            A //= 2 ** get_combo_operand_value(operand, A, B, C)
        
        if opcode == 1:
            B ^= operand
        
        if opcode == 2:
            B = get_combo_operand_value(operand, A, B, C) % 8
        
        if opcode == 3 and A != 0:
            instruction_ptr = operand
            continue

        if opcode == 4:
            B ^= C
        
        if opcode == 5:
            out.append(get_combo_operand_value(operand, A, B, C) % 8)
        
        if opcode == 6:
            B = A // (2 ** get_combo_operand_value(operand, A, B, C))
        
        if opcode == 7:
            C = A // (2 ** get_combo_operand_value(operand, A, B, C))
        
        instruction_ptr += 2
    
    return out

output = get_output(A, B, C)
part1 = ",".join(map(str, output))
print(f"Part 1: {part1}")

A_values = []

for bits in range(8):
    possible_A = bits << ((len(program)-1) * 3)
    if get_output(possible_A, B, C)[-1] == program[-1]:
        A_values.append(possible_A)

next_A_values = []

for offset, correct in enumerate(program[-2::-1], start=2):
    for A in A_values:
        for bits in range(8):
            possible_A = A | (bits << ((len(program)-offset) * 3))
            if get_output(possible_A, B, C)[-offset] == correct:
                next_A_values.append(possible_A)

    next_A_values, A_values = [], next_A_values

part2 = min(A_values)
print(f"Part 2: {part2}")
