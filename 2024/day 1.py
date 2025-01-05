with open("input.txt", "r") as file:
    contents = file.read().split()

contents = [int(i) for i in contents]
seperate = [contents[i:i+2] for i in range(0, len(contents), 2)]
first_list, second_list = zip(*seperate)
first_list, second_list = sorted(first_list), sorted(second_list)

part1 = 0

for first, second in zip(first_list, second_list):
    part1 += abs(first - second)

print(f"Part 1: {part1}")

part2 = 0
second_dictionary = {k: second_list.count(k) for k in second_list}

for first in first_list:
    part2 += first * second_dictionary.get(first, 0)

print(f"Part 2: {part2}")
