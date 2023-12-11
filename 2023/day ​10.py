with open(r"C:\Users\izoya\Desktop\VSPython\aoc 2023\day 10\input.txt") as file:
    inp = file.read().splitlines()

inp = ["."*len(inp[0])] + inp + ["."*len(inp[0])]

for index, line in enumerate(inp):
    inp[index] = "." + line + "."

start_x = 0
start_y = 0

for index, line in enumerate(inp):
    if "S" in line:
        start_x = index
        start_y = line.find("S")

valid_next_coordinates = []
substitute = {*"-|LFJ7"}
if inp[start_x][start_y-1] in "-LF":
    substitute &= {*"-J7"}
    valid_next_coordinates.append((start_x, start_y-1))
if inp[start_x][start_y+1] in "-J7":
    substitute &= {*"-LF"}
    valid_next_coordinates.append((start_x, start_y+1))
if inp[start_x-1][start_y] in "|F7":
    substitute &= {*"|JL"}
    valid_next_coordinates.append((start_x-1, start_y))
if inp[start_x+1][start_y] in "|JL":
    substitute &= {*"|F7"}
    valid_next_coordinates.append((start_x+1, start_y))

for next_x, next_y in valid_next_coordinates:
    seen = set()

    while (current := inp[next_x][next_y]) != "S":
        next_coords = {
            "L": [(next_x, next_y+1), (next_x-1, next_y)],
            "F": [(next_x, next_y+1), (next_x+1, next_y)],
            "7": [(next_x, next_y-1), (next_x+1, next_y)],
            "J": [(next_x-1, next_y), (next_x, next_y-1)],
            "-": [(next_x, next_y-1), (next_x, next_y+1)],
            "|": [(next_x-1, next_y), (next_x+1, next_y)],
        }

        if current not in next_coords:
            break
        
        possibilities = next_coords[current]

        if (start_x, start_y) in possibilities and len(seen) == 0:
            # we just started looping
            possibilities.remove((start_x, start_y))

        for possible in possibilities:
            if possible not in seen:
                seen.add((next_x, next_y))
                next_x, next_y = possible
    else:
        seen.add((start_x, start_y))
        break

print("Part 1:", len(seen)//2)

# we change the S to whatever pipe it's supposed to be
inp[start_x] = inp[start_x][:start_y] + substitute.pop() + inp[start_x][start_y+1:]

current_y = min(y for x, y in seen)
current_x = min(x for x, y in seen if y == current_y)
counter = 0
area = set()

while counter != len(seen):
    min_x = min(x for x, y in seen if y == current_y)
    max_x = max(x for x, y in seen if y == current_y)

    for scan_x in range(min_x, max_x+1):
        if (scan_x, current_y) in seen:
            counter += 1
            continue

        left = current_y - 1
        left_string = ""
        while True:
            if (scan_x, left) not in seen and (scan_x, left) not in area:
                break
            
            if (scan_x, left) in seen and inp[scan_x][left] != "-":
                left_string = inp[scan_x][left] + left_string
            
            left -= 1
        walls = 0

        while left_string:
            if left_string[-2:] in ("LJ", "F7"):
                walls += 2
                left_string = left_string[:-2]
            
            elif left_string[-2:] in ("L7", "FJ"):
                walls += 1
                left_string = left_string[:-2]
            
            else:
                walls += 1
                left_string = left_string[:-1]
        
        # you need to cross an odd number of walls to be considered outside the pipes
        if walls % 2 == 1:
            area.add((scan_x, current_y))

    current_y += 1
        
print("Part 2:", len(area))
