with open("input.txt", "r") as file:
    unparsed_grid = file.read().split("\n")

grid = {}
start = end = 0+0j

# parsing
for line_index, line in enumerate(unparsed_grid):
    for char_index, char in enumerate(line):
        coords = line_index + char_index * 1j
        if char == ".":
            grid[coords] = None
        
        if char == "S":
            grid[coords] = 0
            start = coords
        
        if char == "E":
            grid[coords] = None
            end = coords

def get_four_directions(coordinate: complex):
    for direction in [1, -1, 1j, -1j]:
        yield coordinate + direction

def get_next_position(position: complex) -> complex:
    for next_pos in get_four_directions(position):
        if next_pos in grid and grid[next_pos] is None:
            return next_pos

# running through the maze
current_position = start
steps = 0

while current_position != end:
    next_position = get_next_position(current_position)
    steps += 1
    grid[next_position] = steps
    current_position = next_position

def get_within_reach(initial: complex, cheat_time: int):
    for y_diff in range(-cheat_time, cheat_time+1):
        x_range = abs(cheat_time - abs(y_diff))
        for x_diff in range(-x_range, x_range+1):
            potential = initial + x_diff + y_diff*1j

            if potential not in grid:
                continue

            if grid[initial] > grid[potential]:
                continue

            distance = abs(x_diff) + abs(y_diff)

            yield potential, distance

part1 = part2 = 0

for position in grid:
    for another_position, difference in get_within_reach(position, 2):
        saved_steps = grid[another_position] - grid[position] - difference
        part1 += saved_steps >= 100
    
    for another_position, difference in get_within_reach(position, 20):
        saved_steps = grid[another_position] - grid[position] - difference
        part2 += saved_steps >= 100

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
