# part 1 and 2
instructions = open("input.txt").read().split("\n")

X = 1
cycles = 0
req = {r: 0 for r in range(20, 221, 40)}
display = ""

for line in instructions:
    loops = 1 + (line != "noop")
    for _ in range(loops):
        if X-1 <= cycles % 40 <= X+1:
            display += "#"
        else:
            display += "."

        cycles += 1
        if cycles in req:
            req[cycles] = cycles * X

    if line != "noop":
        X += int(line.split()[1])

print(sum(req.values()))
print("\n".join(display[x:x+40] for x in range(0, 240, 40)))
