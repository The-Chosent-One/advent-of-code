with open("input.txt", "r") as file:
    contents = file.read().split("\n")[:-1]

def is_sorted(differences: list[int]) -> bool:
    # if all differences are positive or negative, the list is sorted
    return all(d < 0 for d in differences) or all(d > 0 for d in differences)

def is_acceptable(differences: list[int]) -> bool:
    return all(1 <= abs(d) <= 3 for d in differences)

contents = [l.split() for l in contents]
reports = [[int(i) for i in l] for l in contents]

part1 = part2 = 0

for report in reports:  
    differences = [report[i] - report[i-1] for i in range(1, len(report))]

    if is_sorted(differences) and is_acceptable(differences):
        part1 += 1
        part2 += 1
        continue

    for i in range(len(report)):
        removed = report[:i] + report[i+1:]
        new_differences = [removed[i] - removed[i-1] for i in range(1, len(removed))]

        if is_sorted(new_differences) and is_acceptable(new_differences):
            part2 += 1
            break
    
    
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
