import re

with open("input.txt", "r") as file:
    contents = file.read().split("\n\n")
    coefficients = [[*map(int, re.findall(r"\d+", lines))] for lines in contents]

def get_tokens(part2=False) -> int:
    tokens = 0
    for a, b, c, d, e, f in coefficients:
        if part2:
            e += 10000000000000
            f += 10000000000000

        y, remainder = divmod(e*b-a*f, b*c-a*d)
        if remainder != 0 or (not part2 and y > 100) or y < 0:
            continue

        x, remainder = divmod(e-c*y, a)
        if remainder != 0 or (not part2 and x > 100) or x < 0:
            continue

        tokens += 3*x + y
    
    return tokens

print(f"Part 1: {get_tokens()}")
print(f"Part 2: {get_tokens(part2=True)}")
