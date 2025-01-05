from itertools import product

with open("input.txt", "r") as file:
    contents = file.read().split()
    contents = ["." * len(contents[0])] + contents + ["." * len(contents[0])]
    contents = [f".{l}." for l in contents]

all_coords = {(x, y) for x in range(len(contents)) for y in range(len(contents[0])) if contents[x][y] != "."}
part1 = part2 = 0

def get_four_directions(x: int, y: int) -> list[tuple[int, int]]:
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

def get_edges(seen: set[tuple[int, int]], start_bounds: tuple[int, int], end_bounds: tuple[int, int]) -> int:
    # V - E + F = 2
    # euler's characteristic, and since a plane has 2 faces, V = E
    # verticles (which are corners) = edges

    # we look across every 2x2 grid and count the number of plants
    # if it's odd, there's a corner
    # if there's two, and both are diagonal, there are two corners
    edges = 0

    for x, y in product(start_bounds, end_bounds):
        top_left = (x, y) in seen
        top_right = (x, y+1) in seen
        bottom_left = (x+1, y) in seen
        bottom_right = (x+1, y+1) in seen

        total_plants = top_left + top_right + bottom_left + bottom_right
        edges += total_plants % 2

        if total_plants == 2 and ((top_left and bottom_right) or (top_right and bottom_left)):
            edges += 2

    return edges
        
# part 1: bfs flood fill
while all_coords:
    seen = set()
    valid = [all_coords.pop()]

    area = perimeter = 0
    sides = 2

    while valid:
        x, y = valid.pop(0)

        if (x, y) in seen:
            continue

        char = contents[x][y]
        
        seen.add((x, y))
        directions = get_four_directions(x, y)

        area += 1
        perimeter += 4

        for next_x, next_y in directions:
            if contents[next_x][next_y] == char:
                valid.append((next_x, next_y))
                perimeter -= 1

    all_coords -= seen
    part1 += area * perimeter
    x_bounds = range(min(x for x, y in seen)-1, max(x for x, y in seen)+2)
    y_bounds = range(min(y for x, y in seen)-1, max(y for x, y in seen)+2)
    edges = get_edges(seen, x_bounds, y_bounds)
    part2 += area * edges

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
