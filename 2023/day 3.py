import re

with open("input.txt", "r") as file:
    inp = file.read()

# using regex (I had fun doing this)
PART_1_RE = re.compile(r"\d{1,3}(?=[^\d\n.])|\d{3}(?=.{137,141}[^\d\n.])|\d\d(?=.{138,141}[^\d\n.])|\d(?=.{139,141}[^\d\n.])|(?<=[^\d\n.])\d{1,3}|(?<=[^\d\n.].{137})\d{3}|(?<=[^\d\n.].{138})\d{2,3}|(?<=[^\d\n.].{139})\d{1,3}|(?<=[^\d\n.].{140})\d{1,3}|(?<=[^\d\n.].{141})\d{1,3}", re.DOTALL)

print(sum(map(int, PART_1_RE.findall(inp))))

part1 = 0

inp = ["."*len(inp[0])] + inp + ["."*len(inp[0])]
for index, line in enumerate(inp):
  inp[index] = "." + line + "."
  

pattern = re.compile(r"\d+")

for x, line in enumerate(inp):
  for match in pattern.finditer(line):
    start, stop = match.span()
    surroundings = inp[x-1][start-1:stop+1] + line[start-1] + line[stop] + inp[x+1][start-1:stop+1]

    if re.findall(r"[^\d\.]", surroundings):
      part1 += int(match.group())
      

print(part1)


part2 = 0

for x, line in enumerate(inp):
  for match in re.finditer("\*", line):
    gear_start, gear_stop = match.span()
    nums = []
    
    for row in (1, -1):
      for num_match in pattern.finditer(inp[x+row]):
        num_start, num_stop = num_match.span()
      
        if gear_start-1 <= num_start <= gear_stop or gear_start <= num_stop <= gear_stop+1:
          nums.append(num_match.group())
    
    for num_match in pattern.finditer(line):
      num_start, num_stop = num_match.span()
      
      if num_stop == gear_start or num_start == gear_stop:
        nums.append(num_match.group())
  
    if len(nums) == 2:
      part2 += int(nums[0]) * int(nums[1])
    
    
print(part2)
