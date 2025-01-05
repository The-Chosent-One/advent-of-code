import re
from functools import cache

with open("input.txt", "r") as file:
    towel_patterns, designs = file.read().split("\n\n")
    towel_patterns = {*re.findall(r"[wubrg]+", towel_patterns)}
    designs = re.findall(r"[wubrg]+", designs)

MAX_SUBSTRING_LENGTH = max(map(len, towel_patterns))

@cache
def get_possibilities(design: str) -> int:
    if design == "":
        return 1
    
    possible = set()

    for index in range(1, MAX_SUBSTRING_LENGTH+1):
        if design[:index] in towel_patterns:
            possible.add(design[index:])
    
    if len(possible) == 0:
        return 0
    
    return sum(map(get_possibilities, possible))

part1 = part2 = 0

for design in designs:
    possibilities = get_possibilities(design)
    part1 += bool(possibilities)
    part2 += possibilities

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
