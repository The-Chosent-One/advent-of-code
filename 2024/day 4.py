with open("input.txt", "r") as file:
    contents = file.read().split("\n")[:-1]

def transpose(contents: list[str]) -> list[str]:
    return ["".join(t) for t in zip(*contents)]

def flip(contents: list[str]) -> list[str]:
    return [s[::-1] for s in contents]

def get_horizontals(row: str) -> int:
    return row.count("XMAS") + row.count("SAMX")

def get_diagonals(section: list[str]) -> int:
    for index, line in enumerate(section):
        section[index] = line[index:] + "." * index
    
    new = transpose(section)
    return new.count("XMAS") + new.count("SAMX")

part1 = part2 = 0

############## PART 1
for _ in range(2):
    contents = transpose(contents)
    for line in contents:
        part1 += get_horizontals(line)

    contents = flip(contents)
    for index in range(4, len(contents) + 1):
        section = contents[index-4:index]
        part1 += get_diagonals(section)

print(f"Part 1: {part1}")

############## PART 2 
# add a border
contents = ["." * len(contents)] + contents + ["." * len(contents)]
contents = [f".{l}." for l in contents]

for line_index, line in enumerate(contents):
    for char_index, char in enumerate(line):
        if char != "A":
            continue
        
        diagonals = [
            contents[line_index-1][char_index-1] + contents[line_index+1][char_index+1], # ↖↘
            contents[line_index-1][char_index+1] + contents[line_index+1][char_index-1]  # ↙↗
        ]
        
        if all(d in ["SM", "MS"] for d in diagonals):
            part2 += 1

print(f"Part 2: {part2}")
