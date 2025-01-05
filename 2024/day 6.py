import re
from collections import defaultdict

with open("input.txt", "r") as file:
    map = file.read().split("\n")

## SET-UP 

obstacles, seen = set(), defaultdict(set)
start_position = None
move_vector = -1
good_magic_obstacles, bad_magic_obstacles = set(), set()

for line_index, line in enumerate(map):
    for match in re.finditer("#", line):
        obstacle_index = match.span()[0]
        obstacles.add(line_index + obstacle_index*1j)
    
    if "^" in line:
        start_position = line_index + line.index("^")*1j
        seen[start_position] = {move_vector}

## MEAT OF THE SOLUTIONS
def simulate_movement(position: complex, move_vector: complex, obstacles: set[complex]):
    while 0 < position.real < len(map) - 1 and 0 < position.imag < len(map[0]) - 1:
        next_position = position + move_vector

        if next_position in obstacles:
            move_vector *= -1j
            yield position, move_vector
            continue
        
        position = next_position
        yield position, move_vector

for next_position, move_vector in simulate_movement(start_position, move_vector, obstacles):
    seen[next_position] |= {move_vector}

    magic_obstacle = next_position + move_vector

    # if there's already an obstacle in front of us or
    # if we've already planted this magic obstacle before
    if magic_obstacle in obstacles | good_magic_obstacles | bad_magic_obstacles:
        continue

    # can't put an obstacle where the guard initially is
    if magic_obstacle == start_position:
        continue

    # restart the simulation of movement from the start,
    # but this time including the magic obstacle
    cache = defaultdict(set)
    for hypothetical_position, move_vector in simulate_movement(start_position, -1, obstacles | {magic_obstacle}):
        # if we've been to any places we've been to
        # with the same movement vector
        if move_vector in cache[hypothetical_position]:
            good_magic_obstacles.add(magic_obstacle)
            break

        cache[hypothetical_position] |= {move_vector}
    else:
        bad_magic_obstacles.add(magic_obstacle)

print(f"Part 1: {len([v for v in seen.values() if v])}")
print(f"Part 2: {len(good_magic_obstacles)}")
