import re
from itertools import cycle
from math import lcm

with open("input.txt") as file:
    inp = file.read()

instructions = inp.split("\n")[0]
mapping = {}
part1 = 0

for start, left, right in re.findall(r"(...) = \((...), (...)\)", inp):
    mapping[start] = [left, right]

node = "AAA"

for char in cycle(instructions):
    index = char == "R"

    if node == "ZZZ":
        break
    
    node = mapping[node][index]
    part1 += 1

print(part1)

counter = 0
nodes = [start for start in mapping if start[-1] == "A"]
steps = []

for char in cycle(instructions):
    index = char == "R"
    counter += 1

    for i, node in enumerate(nodes):
        nodes[i] = mapping[node][index]

    for n in nodes:
        if n[-1] == "Z":
            nodes.remove(n)
            steps.append(counter)

    if nodes == []:
        break

print(lcm(*steps))
