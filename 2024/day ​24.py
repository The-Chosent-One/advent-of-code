import re
import operator

with open("input.txt", "r") as file:
    starting, unparsed_instructions = file.read().split("\n\n")
    values = {name: int(value) for name, value in re.findall(r"([xy]\d+): (\d)", starting)}
    unstructured_instructions = re.findall(r"(.{3}) (AND|XOR|OR) (.{3}) -> (.{3})", unparsed_instructions)
    instructions = {result: set(operations) for *operations, result in unstructured_instructions}

###### PART 1 ######
part1_values = values.copy()
mapping = {"OR": operator.or_, "XOR": operator.xor, "AND": operator.and_}
while unstructured_instructions:
    op1, operation, op2, res = unstructured_instructions.pop(0)

    if op1 in part1_values and op2 in part1_values:
        operation = mapping[operation]
        part1_values[res] = operation(part1_values[op1], part1_values[op2])
        continue

    unstructured_instructions.append((op1, operation, op2, res))

names = sorted((name for name in part1_values if name[0] == "z"), reverse=True)
bin_repr = "".join(str(part1_values[n]) for n in names)
part1 = int(bin_repr, 2)

print(f"Part 1: {part1}")

###### PART 2 ######
def get_name_from_operations(operations: set[str]) -> str | None:
    try:
        return next(name for name, op in instructions.items() if op == operations)
    except StopIteration:
        return None

def get_correct_name(part_operations: set[str]) -> str | None:
    try:
        wrong_operation = next(op for op in instructions.values() if part_operations.issubset(op))
        return (wrong_operation - part_operations).pop()
    except StopIteration:
        return None

def right_the_wrongs(first_incorrect: str, second_incorrect: str) -> None:
    first, second = instructions[first_incorrect], instructions[second_incorrect]
    instructions[first_incorrect] = second
    instructions[second_incorrect] = first
    part2.update({first_incorrect, second_incorrect})
    
part2 = set()
bit_length = len(values) // 2 - 1
prev_carry_name = get_name_from_operations({"x00", "AND", "y00"})

# we basically check for the full adder here, checking for 
# half adder = x ^ y
# result = prev carry ^ half adder
# current carry = x & y
# next carry = current carry | (prev carry & half adder)
for index in range(1, bit_length):
    x_operand = f"x{index:02}"
    y_operand = f"y{index:02}"
    z_result = f"z{index:02}"

    current_carry_name = get_name_from_operations({x_operand, "AND", y_operand})
    half_add_name = get_name_from_operations({x_operand, "XOR", y_operand})
    intermediate_name = get_name_from_operations({prev_carry_name, "AND", half_add_name})

    if intermediate_name is None:
        # either prev_carry_name is wrong or half_add_name is wrong
        if corrected := get_correct_name({prev_carry_name, "AND"}):
            right_the_wrongs(corrected, half_add_name)
            half_add_name = corrected
        
        elif corrected := get_correct_name({half_add_name, "AND"}):
            right_the_wrongs(corrected, prev_carry_name)
            prev_carry_name = corrected
        
        intermediate_name = get_name_from_operations({prev_carry_name, "AND", half_add_name})
    
    result = get_name_from_operations({prev_carry_name, "XOR", half_add_name})
    
    if result != z_result:
        right_the_wrongs(result, z_result)
        result = z_result

    next_carry_name = get_name_from_operations({current_carry_name, "OR", intermediate_name})

    if next_carry_name is None:
        # either current_carry_name or intermediate_name is wrong
        if corrected := get_correct_name({current_carry_name, "OR"}):
            right_the_wrongs(corrected, intermediate_name)
            intermediate_name = corrected
        elif corrected := get_correct_name({intermediate_name, "OR"}):
            right_the_wrongs(corrected, current_carry_name)
            current_carry_name = corrected

        next_carry_name = get_name_from_operations({current_carry_name, "OR", intermediate_name})

    prev_carry_name = next_carry_name

print("Part 2:", ",".join(sorted(part2)))
