# part 1

import re
commands = open("input.txt").read()

history = []
ignored = set()
potential = {}
confirmed = {}

for cd, ls in re.findall(r"cd (.+)|ls\n((?:[^\$]+\n?)+)", commands):
    if cd:
        history.pop() if cd == ".." else history.append(cd)
    if ls:
        current_path = "-".join(history)
        if any(current_path in i for i in ignored):
            continue

        files_size = sum(map(int, re.findall(r"\d+", ls)))
        dirs = re.findall(r"dir (.+)", ls)
        
        if len(dirs) == 0 and files_size <= 100000:
            confirmed[current_path] = files_size
        elif files_size > 100000:
            # ignore all future paths
            if current_path != "/":
                ignored.add(current_path)
        else:
            potential[current_path] = [files_size, *dirs]

for potential_path, (file_size, *components) in [*potential.items()][::-1]:
    total = file_size
    for path in components:
        if (num := confirmed.get(f"{potential_path}-{path}")):
            total += num
        elif any(potential_path in i for i in ignored):
            total = 1e8
            break
    
    if total > 100000:
        ignored.add(potential_path)
    else:
        confirmed[potential_path] = total

print(sum(confirmed.values()))



# part 2
history = []
potential = {}
confirmed = {}

for cd, ls in re.findall(r"cd (.+)|ls\n((?:[^\$]+\n?)+)", commands):
    if cd:
        history.pop() if cd == ".." else history.append(cd)
    if ls:
        current_path = "-".join(history)
        files_size = sum(map(int, re.findall(r"\d+", ls)))
        dirs = re.findall(r"dir (.+)", ls)
        
        if len(dirs) == 0:
            confirmed[current_path] = files_size
        else:
            potential[current_path] = [files_size, *dirs]

for potential_path, (file_size, *components) in [*potential.items()][::-1]:
    total = file_size
    for path in components:
        if (num := confirmed.get(f"{potential_path}-{path}")):
            total += num
    
    confirmed[potential_path] = total

print([*filter(lambda a: a > 0, sorted([v - 3598596 for v in confirmed.values()]))][0]+3598596)
