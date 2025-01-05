import re
from graphlib import TopologicalSorter
from collections import defaultdict

with open("input.txt", "r") as file:
    rules, updates = file.read().split("\n\n")

INT_REGEX = re.compile(r"\d+")

rules = [[*map(int, INT_REGEX.findall(r))] for r in rules.split("\n")]
updates = [[*map(int, INT_REGEX.findall(u))] for u in updates.split("\n")]
incorrect_updates = []

after = defaultdict(set)
before = defaultdict(set)
part1 = part2 = 0

def is_correctly_ordered(update: list[int], index: int, num: int):
    before_nums, after_nums = set(update[:index]), set(update[index+1:])
    return not (before_nums & after[num]) or (after_nums & before[num])

for before_num, after_num in rules:
    before[after_num] |= {before_num}
    after[before_num] |= {after_num}

for update in updates:
    for index, num in enumerate(update):
        if not is_correctly_ordered(update, index, num):
            incorrect_updates.append(update)
            break
    # correctly ordered updates
    else:
        part1 += update[len(update)//2]

print(f"Part 1: {part1}")

for pages in incorrect_updates:
    master_rules = {}
    for page in pages:
        master_rules[page] = after[page] & set(pages)

    ts = TopologicalSorter(master_rules)
    reordered = list(ts.static_order())[::-1]
    
    part2 += reordered[len(reordered)//2]

print(f"Part 2: {part2}")
