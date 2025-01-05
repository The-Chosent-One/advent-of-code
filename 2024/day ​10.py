from collections import defaultdict

with open("input.txt", "r") as file:
    contents = file.read().split("\n")
    map = [[*map(int, line)] for line in contents]

# padding
map = [[-1] * len(map[0])] + map + [[-1] * len(map[0])]
map = [[-1, *line, -1] for line in map]

trailheads = []

for line_index, line in enumerate(map):
    for char_index, char in enumerate(line):
        if char == 0:
            trailheads.append((line_index, char_index))

def get_score(x: int, y: int, seen: defaultdict[int], part2=False) -> int:
    current_height = map[x][y]

    if (x, y) in seen:
        return seen[(x, y)] if part2 else 0

    if current_height == 9:
        score = (x, y) not in seen
        seen[(x, y)] += 1
        return score
    
    directions = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    valid = []

    for next_x, next_y in directions:
        next_height = map[next_x][next_y]

        if next_height - current_height == 1:
            valid.append((next_x, next_y))
    
    score = sum(get_score(valid_x, valid_y, seen, part2=part2) for valid_x, valid_y in valid)
    seen[(x, y)] += score
    
    return score

part1 = part2 = 0

for x, y in trailheads:
    part1 += get_score(x, y, defaultdict(int))
    part2 += get_score(x, y, defaultdict(int), part2=True)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
