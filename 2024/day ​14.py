import re
from functools import reduce
from itertools import product

with open("input.txt", "r") as file:
    contents = file.read().split("\n")
    robots = [[*map(int, re.findall(r"-?\d+", line))] for line in contents]

SPACE_HEIGHT = 103
SPACE_WIDTH = 101

def get_positions(seconds: int):
    for x, y, vx, vy in robots:
        new_x = (x + vx * seconds) % SPACE_WIDTH
        new_y = (y + vy * seconds) % SPACE_HEIGHT

        yield new_x, new_y
    
def get_safety_factor(seconds: int) -> int:
    quadrants = [0] * 4

    for x, y in get_positions(seconds):
        if x == SPACE_WIDTH // 2 or y == SPACE_HEIGHT // 2:
            continue

        quadrant_number = 0
        
        # right half
        quadrant_number += x in range(SPACE_WIDTH // 2 + 1, SPACE_WIDTH)
        
        # bottom half
        quadrant_number += 2 * (y in range(SPACE_HEIGHT // 2 + 1, SPACE_HEIGHT))
        
        quadrants[quadrant_number] += 1
    
    return reduce(lambda x,y: x*y, quadrants)

def print_visualisation(positions: set[tuple[int, int]]) -> None:
    to_print = ""
    for y, x in product(range(SPACE_HEIGHT), range(SPACE_WIDTH)):
        to_print += "O" if (x, y) in positions else "."

        if x == (SPACE_WIDTH - 1):
            to_print += "\n"
    
    print(to_print)

def heuristic(positions: set[tuple[int, int]]) -> bool:
    # we will only return True if half of the points have a neighbouring robot
    # to make it simple we'll only do the four directions,
    # up, down, left, right

    qualifies_positions = positions.copy()
    qualifies = 0

    while qualifies_positions:
        x, y = qualifies_positions.pop()
        directions = {(x-1, y), (x+1, y), (x, y-1), (x, y+1)}

        qualifies += len(directions & positions)
        qualifies_positions -= directions
    
    return qualifies >= (len(robots) // 2)

def get_christmas_tree() -> int:
    seconds = 0
    while True:
        seconds += 1
        positions = {*get_positions(seconds)}

        if heuristic(positions):
            print_visualisation(positions)
            if input("Type anything if this is THE ONE: "):
                return seconds

print(f"Part 1: {get_safety_factor(100)}")
print(f"Part 2: {get_christmas_tree()}")
