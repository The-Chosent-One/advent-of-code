import re

with open("input.txt", "r") as file:
    inp = file.read()

pattern = re.compile(r"(?P<b>\d+(?= b))|(?P<r>\d+(?= r))|(?P<g>\d+(?= g))")

part1 = 0
RED = 12
GREEN = 13
BLUE = 14

for number, line in enumerate(inp.split("\n"), start=1):
    for blue, red, green in pattern.findall(line):
        if blue and int(blue) > BLUE:
            break

        if red and int(red) > RED:
            break

        if green and int(green) > GREEN:
            break

    else:
        part1 += number

print(part1)

part2 = 0

for number, line in enumerate(inp.split("\n"), start=1):
    max_blue = max_red = max_green = 0

    for blue, red, green in pattern.findall(line):
        if blue:
            max_blue = max(int(blue), max_blue)
        
        if red:
            max_red = max(int(red), max_red)

        if green:
            max_green = max(int(green), max_green)

    part2 += max_green * max_blue * max_red

print(part2)
