from collections import defaultdict
from math import log10

with open("input.txt", "r") as file:
    contents = [int(r) for r in file.read().split()]

def get_stones(blink_number: int) -> int:
    rocks = {r: 1 for r in contents}
    new_rocks = defaultdict(int)

    for _ in range(blink_number):
        for rock, num in rocks.items():
            if rock == 0:
                new_rocks[1] += num
            elif (num_of_digits := int(log10(rock))+1) % 2 == 0:
                q, r = divmod(rock, 10 ** (num_of_digits // 2))
                new_rocks[q] += num
                new_rocks[r] += num
            else:
                new_rocks[rock * 2024] += num

        new_rocks, rocks = defaultdict(int), new_rocks
    
    return sum(rocks.values())

print(f"Part 1: {get_stones(25)}")
print(f"Part 2: {get_stones(75)}")
