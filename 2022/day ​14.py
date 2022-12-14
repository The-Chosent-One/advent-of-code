# part 1 and 2
from itertools import pairwise

unparsed_lines = open("input.txt").read().split("\n")
walls = set()
still_sand = set()

for line in unparsed_lines:
    partitions = line.split(" -> ")
    for p1, p2 in pairwise(partitions):
        x1, y1 = map(int, p1.split(","))
        x2, y2 = map(int, p2.split(","))

        if x1 - x2:
            walls |= {(x, y1) for x in range(x1, x2 + 1) or range(x2, x1 + 1)}
        
        if y1 - y2:
            walls |= {(x1, y) for y in range(y1, y2 + 1) or range(y2, y1 + 1)}

threshold = max(walls, key=lambda t:t[1])[1]
floor = threshold + 2

def next_tile(current_coords: tuple[int]) -> tuple[int] | None:
    x, y = current_coords
    for dx in [0, -1, 1]:
        next_x, next_y = x + dx, y + 1        
        if (next_x, next_y) in walls or (next_x, next_y) in still_sand:
            continue
        
        # uncomment for part 2
        # if next_y == floor:
        #     return None
        
        return (next_x, next_y)

initial = (500, 0)
queue = [initial]

while queue:
    coords = queue[-1]
    next_coords = next_tile(coords)

    # comment out for part 2
    if coords[1] > threshold:
        break

    if next_coords is None:
        still_sand.add(coords)
        queue.pop()
        continue

    queue.append(next_coords)

print(len(still_sand))
