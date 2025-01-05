with open("input.txt", "r") as file:
    grid = file.read().split("\n")

maze = {}
start = 0+0j
end = 0+0j
initial_direction = 1j

# parsing
for x, line in enumerate(grid):
    for y, char in enumerate(line):
        coords = x + y*1j
        if char in "ES.":
            maze[coords] = None
        
        if char == "S":
            start = coords
        
        if char == "E":
            end = coords

def get_movements(position: complex, direction: complex):
    for turn in [1, 1j, -1j]:
        yield position + direction * turn, direction * turn

# part 1 function
def get_next_positions(initial: complex, direction: complex, current_points: int) -> list[tuple[complex, complex, complex]]:
    ret = []

    for next_position, next_direction in get_movements(initial, direction):
        if next_position not in maze:
            continue
        
        new_points = current_points + 1
        if next_direction != direction:
            # here, we treat a turn as a move by itself,
            # thus we add 1000 in total and don't go
            # to our next position
            new_points += 999
            next_position = initial
        
        ret.append((next_position, next_direction, new_points))
    
    return ret

# we first get the next position from the start and given the initial direction
queue = get_next_positions(start, initial_direction, 0)

while queue:
    position, direction, points = queue.pop()

    # if it's our first time visiting this position
    if maze[position] is None:
        maze[position] = {direction: points}
    # if we've been here before with the same direction,
    # check to see that we're now here with lower points
    elif direction in maze[position] and points >= maze[position][direction]:
        continue
    else:
        maze[position][direction] = points

    if position == end:
        continue
    
    queue.extend(get_next_positions(position, direction, points))

part1 = min(maze[end].values())
print(f"Part 1: {part1}")

# backtrack for part 2
def get_valid_paths(position: complex, rev_direction: complex, seen: set[complex]) -> list[tuple[complex, complex]]:
    # we first get the points from our position
    points = maze[position][rev_direction]
    # and then we get the previous position we've been to
    prev_position = position - rev_direction
    valid = []

    # if the previous position is invalid
    if prev_position not in maze:
        return valid

    for direction in maze[prev_position]:
        # the previous position's direction is more than
        # the amount of points we have now, thus
        # we don't need to follow that direction
        if maze[prev_position][direction] > points:
            continue
        
        seen.add(prev_position)
        valid.append((prev_position, direction))
        
    return valid

# get the direction(s) where we reached the end with the lowest points
paths = [(end, d) for d,p in maze[end].items() if p == part1]
seen = {start, end}

# keep backtracking
while paths:
    position, rev_direction = paths.pop()
    paths.extend(get_valid_paths(position, rev_direction, seen))

print(f"Part 2: {len(seen)}")
