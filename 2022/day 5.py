# part 1 and 2

import re

input_lines = open("input.txt").read().split("\n")
unparsed_boxes, unparsed_instructions = input_lines[:9], input_lines[10:]

boxes = [""] + ["".join(i).strip()[:-1] for i in zip(*unparsed_boxes)][1::4]
instructions = [[*map(int,re.findall(r"\d+", i))] for i in unparsed_instructions]

for num, origin, destination in instructions:
    boxes[destination] = boxes[origin][:num][::-1] + boxes[destination] # remove [::-1] for part 2
    boxes[origin] = boxes[origin][num:]

print("".join(s[0] for s in boxes[1:]))
