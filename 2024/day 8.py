from collections import defaultdict
from itertools import combinations

with open("input.txt", "r") as file:
    grid = file.read().split("\n")

antennas = defaultdict(set)
part1_antinodes, part2_antinodes = set(), set()
MAXIMUM_X, MAXIMUM_Y = len(grid[0]), len(grid)

for line_index, line in enumerate(grid):
    for char_index, char in enumerate(line):
        if char == ".":
            continue
        
        antennas[char].add(char_index + line_index*1j)

def in_bounds(point: complex) -> bool:
    return 0 <= point.real < MAXIMUM_X and 0 <= point.imag < MAXIMUM_Y

def get_points(point: complex, pivot: complex) -> set[complex]:
    antinodes = {point, pivot}
    for _ in range(2):
        relative_distance = pivot - point
        mult = 1
        while in_bounds(antinode := pivot + mult*relative_distance):
            antinodes.add(antinode)
            mult += 1
        
        point, pivot = pivot, point

    return antinodes

for antenna_points in antennas.values():
    for pivot, point in combinations(antenna_points, 2):
        part1_antinodes |= {2*pivot - point, 2*point - pivot}
        part2_antinodes |= get_points(point, pivot)

# trim for out of map
part1 = set(filter(in_bounds, part1_antinodes))

print(f"Part 1: {len(part1)}")
print(f"Part 2: {len(part2_antinodes)}")
