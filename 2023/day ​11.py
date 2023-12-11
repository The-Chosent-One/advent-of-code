from itertools import combinations

with open("input.txt") as file:
    inp = file.read().splitlines()

ADDITIONAL = 1000000 - 1
empty_rows = {index for index, line in enumerate(inp) if all(char == "." for char in line)}
empty_cols = {index for index in range(len(inp)) if all(line[index] == "." for line in inp)}
galaxies = {(x, y) for x, line in enumerate(inp) for y, char in enumerate(line) if char == "#"}

ans = 0

for (x1, y1), (x2, y2) in combinations(galaxies, 2):
    final_x1, final_y1, final_x2, final_y2 = x1, y1, x2, y2
    for row in empty_rows:
        final_x1 += ADDITIONAL * (row < x1)
        final_x2 += ADDITIONAL * (row < x2)
    
    for col in empty_cols:
        final_y1 += ADDITIONAL * (col < y1)
        final_y2 += ADDITIONAL * (col < y2)

    ans += abs(final_x1 - final_x2) + abs(final_y1 - final_y2)

print(ans)
