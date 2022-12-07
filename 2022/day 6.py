# part 1 and 2
line = open("input.txt").read()

# change all 4 to 14 for part 2
for chars in range(4, len(line)):
    test_string = line[chars-4:chars]

    if len({*test_string}) == 4:
        print(chars)
        break
