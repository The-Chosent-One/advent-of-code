import re
from collections import Counter

with open("input.txt", "r") as file:
  inp = re.findall(r"(.{5}) (\d+)", file.read())
 
inp = [[hand, int(bid)] for hand, bid in inp]

mapping = {"T": "a", "J": "b", "Q": "c", "K": "d", "A": "e"}

# strongest to weakest
pattern_strength = [
  r"(.)(?:\1){4}",
  r"(.)(?:\1){3}",
  r"(.)\1(.)\2{2}|(.)\3{2}(.)\4",
  r"(.)\1{2}",
  r"(.)\1(?:.(.)\2|(.)\3.)|.(.)\4(.)\5",
  r"(.)\1"
]
part1 = part2 = 0

def transform(hand, part_2=False):
  if part_2:
    hand = hand.replace("J", "1")
  for current, replace in mapping.items():
    hand = hand.replace(current, replace)
    
  return hand

def sorting(info, part_2=False):
  hand, _ = info
  psuedo_hand = hand
  
  if part_2:
    counts = Counter(hand)
    replacement = "J"
    for card in sorted(counts, key=counts.get, reverse=True):
      if card != "J":
        replacement = card
        break
    
    psuedo_hand = hand.replace("J", replacement)
    
  arranged = "".join(sorted(psuedo_hand))
  
  for strength, pattern in enumerate(pattern_strength):
    if re.search(pattern, arranged):
      return (7 - strength, transform(hand, part_2=part_2))
  
  return (1, transform(hand, part_2=part_2))

def part2_sorting(info):
  return sorting(info, part_2=True)

part1_inp = sorted(inp, key=sorting)
part2_inp = sorted(inp, key=part2_sorting)

for rank, (hand, bid) in enumerate(part1_inp, start=1):
  part1 += rank * bid

for rank, (hand, bid) in enumerate(part2_inp, start=1):
  part2 += rank * bid

print(part1, part2)
