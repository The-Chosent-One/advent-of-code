import re 

with open("input.txt", "r") as file:
  inp = file.read().split("\n\n")

pattern = re.compile(r"\d+")

seeds = [*map(int, pattern.findall(inp[0]))]

# part 1
def transform(seeds, mapping):
  original = seeds.copy()
  transformed = []
  
  for destination, source, length in mapping:
    index = 0
    while index != len(original):
      seed = original[index]
      if source <= seed < source + length:
        transformed.append(seed + destination - source)
        original.remove(seed)
      else:
        index += 1
  
  return original + transformed
  
for lines in inp[1:]:
  str_mapping = re.findall(r"(\d+) (\d+) (\d+)", lines) 
  mapping = [[int(i) for i in l] for l in str_mapping]
  
  seeds = transform(seeds, mapping)

print(min(seeds))

# part 2
str_seeds = re.findall(r"(\d+) (\d+)", inp[0])
seed_ranges = []

for start, length in str_seeds:
  start, length = int(start), int(length)
  seed_ranges.append([start, start+length-1])

for lines in inp[1:]:
  str_mapping = re.findall(r"(\d+) (\d+) (\d+)", lines)
  mapping = {}
  
  for destination, source, length in str_mapping:
    destination, source, length = int(destination), int(source), int(length)
    mapping[(source, source+length-1)] = destination - source
  
  new_seed_ranges = []
  
  for (start, stop), change in mapping.items():
    index = 0
    while index != len(seed_ranges):
      seed_start, seed_stop = seed_ranges[index]
      
      # case 1:
      # if the whole of seed range is in the
      # range we need to change 
      if seed_start >= start and seed_stop <= stop:
        new_seed_ranges.append([seed_start+change, seed_stop+change])
        del seed_ranges[index]
        continue
      
      # case 2:
      # if the seed range is larger than the 
      # range we need to change
      if seed_start < start and seed_stop > stop:
        new_seed_ranges.append([start+change, stop+change])
        seed_ranges.extend([
          [seed_start, start-1],
          [stop+1, seed_stop]
        ])
        del seed_ranges[index]
        continue
      
      # case 3:
      # if only the end of seed range intersects
      # with the range we need to change
      if start <= seed_stop <= stop:
        new_seed_ranges.append([start+change, seed_stop+change])
        seed_ranges.append([seed_start, start-1])
        del seed_ranges[index]
        continue
      
      # case 4:
      # if the range intersects the other way
      if start <= seed_start <= stop:
        new_seed_ranges.append([seed_start+change, stop+change])
        seed_ranges.append([stop+1, seed_stop])
        del seed_ranges[index]
        continue
      
      index += 1
  
  seed_ranges = seed_ranges + new_seed_ranges

print(min(seed_ranges, key=lambda l:l[0])[0])
