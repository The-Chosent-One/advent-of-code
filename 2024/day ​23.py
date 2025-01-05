from collections import defaultdict
from itertools import combinations
from functools import reduce

with open("input.txt", "r") as file:
    connections = file.read().split("\n")

computers = defaultdict(set)

for conn in connections:
    first, second = sorted(conn.split("-"))
    computers[first].add(second)
    computers[second].add(first)

def get_largest_clique(clique: set[str], neighbour: str, seen: list[set[str]]):
    if clique in seen:
        return set()
    
    if not all(neighbour in computers[c] for c in clique):
        return clique

    seen.append(clique.copy())
    clique.add(neighbour)
    common_neighbours = reduce(lambda n1,n2: n1&n2, [computers[c] for c in clique])

    largest = clique

    for new_neighbour in common_neighbours:
        largest = max(get_largest_clique(clique.copy(), new_neighbour, seen), largest, key=len)

    return largest

part1 = []
seen = []
largest = set()

for computer, connected in computers.items():
    # part 2
    for neighbour in connected:
        largest = max(get_largest_clique({computer}, neighbour, seen), largest, key=len)

    # part 1
    if computer[0] != "t":
        continue

    for first, second in combinations(connected, 2):
        if first in computers[second] and {computer, first, second} not in part1:
            part1.append({computer, first, second})
    
print(f"Part 1: {len(part1)}")
print(f"Part 2: {','.join(sorted(largest))}")
