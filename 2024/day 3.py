import re

MUL_REGEX = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
DO_DONT_REGEX = re.compile(r"do\(\).*?don't\(\)")

def get_mul_result(string: str) -> int:
    return sum(int(first_num) * int(second_num) for first_num, second_num in MUL_REGEX.findall(string))

with open("input.txt", "r") as file:
    contents = file.read().replace("\n", "")
    contents = "do()" + contents + "don't()"

part1 = get_mul_result(contents)
part2 = sum(get_mul_result(enabled) for enabled in DO_DONT_REGEX.findall(contents))

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
