import re 

with open("input.txt", "r") as file:
  inp = file.read().split("\n")

pattern = re.compile(r"\d+")
part1 = part2 = 0
tickets = [1] * len(inp)

for line in inp:
  winning, nums = [*map(pattern.findall, line.split("|"))]
  winning = set([int(n) for n in winning][1:])
  nums = {*map(int, nums)}
  
  winning_nums = len(nums & winning)
  if winning_nums:
    part1 += 2 **(winning_nums - 1)
  
  current_tickets = tickets.pop(0)
  part2 += current_tickets
  
  for index in range(winning_nums):
    tickets[index] += current_tickets
  
print(part1)
print(part2)
