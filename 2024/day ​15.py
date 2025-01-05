with open("input.txt", "r") as file:
    grid, directions = file.read().split("\n\n")
    grid = grid.split("\n")
    directions = directions.replace("\n", "")
    
walls: set[complex] = set()
boxes: set[complex] = set()
robot = 0+0j

PART2_BOX = tuple[complex, complex]

for x, line in enumerate(grid):
    for y, char in enumerate(line):
        if char == "#":
            walls.add(x + y*1j)
        
        if char == "O":
            boxes.add(x + y*1j)
        
        if char == "@":
            robot = x + y*1j

def get_box_next_position(boxes: set[complex], box: complex, movement: complex) -> complex:
    while box in boxes:
        box += movement
    
    return box

def can_move_boxes(boxes: set[PART2_BOX], fat_box: PART2_BOX, movement: complex, boxes_to_move: list[PART2_BOX]) -> bool:
    boxes = boxes.difference({fat_box})
    fat_box = fat_box[0] + movement, fat_box[1] + movement
    
    if any(box in walls for box in fat_box):
        return False

    more_boxes = [box for box in boxes if fat_box[0] in box or fat_box[1] in box]
    if len(more_boxes) == 0:
        return True
    
    boxes_to_move.extend(more_boxes)
    return all(can_move_boxes(boxes, box, movement, boxes_to_move) for box in more_boxes)

def get_gps(boxes: set[complex] | set[PART2_BOX], robot: complex, part2: bool = False) -> int:
    for direction in directions:
        arrow_to_complex = {"^": -1, ">": 1j, "v": 1, "<": -1j}
        movement = arrow_to_complex[direction]

        next_position = robot + movement

        if next_position in walls:
            continue
        
        # part 1
        if not part2 and next_position in boxes:
            box_next_position = get_box_next_position(boxes, next_position, movement)
            if box_next_position in walls:
                continue

            boxes.remove(next_position)
            boxes.add(box_next_position)
        
        # part 2
        if part2 and any(next_position in fat_box for fat_box in boxes):
            boxes_to_move = [*filter(lambda fat_box: next_position in fat_box, boxes)]
            moveable = can_move_boxes(boxes, boxes_to_move[0], movement, boxes_to_move)
            if not moveable:
                continue

            new_boxes = [(b1 + movement, b2 + movement) for (b1, b2) in boxes_to_move]
            boxes.difference_update(boxes_to_move)
            boxes.update(new_boxes)
        
        robot = next_position
    
    if part2:
        return int(sum(b1.real*100 + b1.imag for b1, _ in boxes))

    return int(sum(box.real*100 + box.imag for box in boxes))

part1 = get_gps(boxes.copy(), robot)
print(f"Part 1: {part1}")


# doubling the width of everything
new_walls = set()
for wall in walls:
    new_walls |= {wall.real + wall.imag*2j, wall.real + wall.imag*2j+1j}

walls = new_walls

boxes = {(b.real + b.imag*2j, b.real + b.imag*2j+1j) for b in boxes}
robot = robot.real + robot.imag*2j

part2 = get_gps(boxes.copy(), robot, part2=True)
print(f"Part 2: {part2}")
