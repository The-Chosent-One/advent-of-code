import re
from math import ceil, floor, sqrt

with open("input.txt", "r") as file:
  inp = file.read()

pattern = re.compile(r"(\d+) +(\d+) +(\d+) +(\d+)")
inp_part1 = [*zip(*pattern.findall(inp))]
inp_part1 = [[int(n) for n in l] for l in inp_part1]
part1 = 1

def get_min_max(t, d):
  # minimum, maximum
  return floor((t-sqrt(t**2-4*d))/2+1), ceil((t+sqrt(t**2-4*d))/2-1)

for time, distance in inp_part1:
  minimum, maximum = get_min_max(time, distance)
  
  part1 *= maximum - minimum + 1

print(part1)

time, distance = [int("".join(n)) for n in pattern.findall(inp)]
minimum, maximum = get_min_max(time, distance)

# part 2
print(maximum - minimum + 1)
