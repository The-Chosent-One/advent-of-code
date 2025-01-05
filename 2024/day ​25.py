from itertools import product

with open("day 25/input.txt", "r") as file:
    schematics = file.read().split("\n\n")

def transpose(schematic: list[str]) -> list[str]:
    return ["".join(s) for s in zip(*schematic)]

keys = set()
locks = set()

for schematic in schematics:
    schematic = schematic.split("\n")
    category = keys if schematic[0] == "." * 5 else locks

    shape = tuple((row.count("#") - 1) for row in transpose(schematic))
    category.add(shape)

part1 = 0

for lock in locks:
    for possible_key in product(*[range(5-n+1) for n in lock]):
        part1 += possible_key in keys

print(f"Part 1: {part1}")
