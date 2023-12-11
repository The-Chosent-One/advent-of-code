import re

with open("input.txt", "r") as file:
    inp = file.read().splitlines()

ans = 0
part2 = False

for line in inp:
    nums = [*map(int, re.findall(r"-?\d+", line))][::(-1)**(part2)]
    ans += nums[-1]

    while any(nums):
        for index in range(1, len(nums)):
            nums[index-1] = nums[index] - nums[index-1]
    
        nums.pop()
        ans += nums[-1]

print(ans)
