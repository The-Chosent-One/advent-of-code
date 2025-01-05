import re

with open("input.txt", "r") as file:
    walls = [*map(int, re.findall(r"\d+", file.read()))]
    walls = [complex(*walls[i:i+2]) for i in range(0, len(walls), 2)]

MAX_X = MAX_Y = 6
BYTES_FALLING = 12

if len(walls) > 1000:
    MAX_X = MAX_Y = 70
    BYTES_FALLING = 1024

START, END = 0+0j, MAX_X + MAX_Y*1j
spaces = {x + y*1j for x in range(MAX_X+1) for y in range(MAX_Y+1)}

def get_fastest_path(spaces: set[complex], bytes_falling: int) -> int:
    spaces.difference_update(walls[:bytes_falling])
    spaces = {coord: float("inf") for coord in spaces}

    queue = [(START, 0)]

    while queue:
        position, steps = queue.pop(0)

        if spaces[position] <= steps:
            continue

        next_positions = [position+change for change in (1, -1, 1j, -1j) if position+change in spaces]
        spaces[position] = steps

        if position == END:
            break

        steps += 1
        queue.extend((next_position, steps) for next_position in next_positions)
    
    return spaces[END]

part1 = get_fastest_path(spaces.copy(), BYTES_FALLING)
print(f"Part 1: {part1}")

lower_bound, upper_bound = BYTES_FALLING, len(walls)
while upper_bound - lower_bound != 1:
    mid = (lower_bound + upper_bound) // 2

    path = get_fastest_path(spaces.copy(), mid)

    if path == float("inf"):
        upper_bound = mid
    else:
        lower_bound = mid

last_wall = walls[lower_bound]
print(f"Part 2: {int(last_wall.real)},{int(last_wall.imag)}")
