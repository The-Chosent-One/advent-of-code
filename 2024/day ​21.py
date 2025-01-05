import re
from itertools import pairwise
from functools import cache

with open("input.txt", "r") as file:
    codes = file.read().split("\n")

numerical_pad = [
    [None, "^<", "^", "^>", "^^<", "^^", "^^>", "^^^<", "^^^", "^^^>", ">"],   # 0
    [">v", None, ">", ">>", "^", "^>", "^>>", "^^", "^^>", "^^>>", ">>v"],     # 1
    ["v", "<", None, ">", "<^", "^", "^>", "<^^", "^^", "^^>", "v>"],          # 2
    ["<v", "<<", "<", None, "<<^", "<^", "^", "<<^^", "<^^", "^^", "v"],       # 3
    [">vv", "v", "v>", "v>>", None, ">", ">>", "^", "^>", "^>>", ">>vv"],      # 4
    ["vv", "<v", "v", "v>", "<", None, ">", "<^", "^", "^>", "vv>"],           # 5
    ["<vv", "<<v", "<v", "v", "<<", "<", None, "<<^", "<^", "^", "vv"],        # 6
    [">vvv", "vv", "vv>", "vv>>", "v", "v>", "v>>", None, ">", ">>", ">>vvv"], # 7
    ["vvv", "<vv", "vv", "vv>", "<v", "v", "v>", "<", None, ">", "vvv>"],      # 8
    ["<vvv", "<<vv", "<vv", "vv", "<<v", "<v", "v", "<<", "<", None, "vvv"],   # 9
    ["<", "^<<", "<^", "^", "^^<<", "<^^", "^^", "^^^<<", "<^^^", "^^^", None] # A
]

directional_pad = {
    "<": {">": ">>", "v": ">", "^": ">^", "A": ">>^", "<": ""},
    "v": {"<": "<", "^": "^", ">": ">", "A": "^>", "v": ""},
    ">": {"<": "<<", "^": "<^", "v": "<", "A": "^", ">": ""},
    "^": {"<": "v<", "v": "v", ">": "v>", "A": ">", "^": ""},
    "A": {"<": "v<<", "^": "<", "v": "<v", ">": "v", "A": ""}
}

@cache
def get_length(origin: str, destination: str, rounds: int) -> int:
    result = directional_pad[origin][destination] + "A"

    if rounds == 1:
        return len(result)

    return sum(get_length(o, d, rounds-1) for o, d in pairwise("A" + result))

part1 = part2 = test = 0

for code in codes:
    to_press = "A"
    current = 10
    for char in code:
        char = int(char) if char != "A" else 10
        to_press += numerical_pad[current][char] + "A"
        current = char

    num = int(re.findall(r"\d+", code)[0])
    for origin, destination in pairwise(to_press):
        part1 += num * get_length(origin, destination, 2)
        part2 += num * get_length(origin, destination, 25)
        
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
