# part 1
import re

lines = open("input.txt").read().split("\n")
PAIRS = [[*map(int, re.findall(r"-?\d+", s))] for s in lines]

def unique_ranges(ranges: list[range], final_ranges: list[range]) -> list[range]:
    ranges.sort(reverse=True, key=len)

    for cannot_exist_range in ranges:
        if len(cannot_exist_range) == 0:
            continue
        for r in final_ranges:
            if cannot_exist_range.start in r and cannot_exist_range.stop - 1 in r:
                break
            if r.start in cannot_exist_range and r.stop - 1 in cannot_exist_range:
                temp_ranges = [range(cannot_exist_range.start, r.start), range(r.stop, cannot_exist_range.stop)]
                unique_ranges(temp_ranges, final_ranges)
                break
            if cannot_exist_range.start in r:
                cannot_exist_range = range(r.stop, cannot_exist_range.stop)
            if cannot_exist_range.stop in r:
                cannot_exist_range = range(cannot_exist_range.start, r.start)
        else:
            final_ranges.append(cannot_exist_range)


def cannot_exist(y_level: int, part_2_threshold: int = 0) -> int:
    cannot_exist = []
    exclude = set()

    for sx, sy, bx, by in PAIRS:
        length = abs(sx - bx) + abs(sy - by)
        diff = abs(y_level - sy) - length
        if diff > 0:
            continue
        
        length_at_y_level = abs(length - abs(y_level - sy))
        if part_2_threshold:
            cannot_exist.append(range(max(0, sx - length_at_y_level), min(sx + length_at_y_level + 1, part_2_threshold + 1)))
        else:
            cannot_exist.append(range(sx - length_at_y_level, sx + length_at_y_level + 1))

        # where beacons already exist
        if by == y_level:
            exclude.add(bx)

    final_ranges = []
    unique_ranges(cannot_exist, final_ranges)

    if part_2_threshold:
        return final_ranges
    else:
        return sum(map(len, final_ranges)) - len(exclude)

print(cannot_exist(2000000))

# part 2
# takes like 70 seconds to run oops, but can't be bothered to find optimisations
threshold = 4000000
for y in range(threshold + 1):
    final_ranges = cannot_exist(y, threshold)
    num = sum(map(len, final_ranges))

    if num != threshold + 1:
        final_ranges.sort(key=lambda r: r.start)
        if final_ranges[0].start != 0:
            x = final_ranges[0].start
        if final_ranges[-1].stop != threshold + 1:
            x = final_ranges[-1].stop
        
        for index, r in enumerate(final_ranges):
            if r.stop != final_ranges[index + 1].start:
                x = r.stop
                break
        
        print(x * 4000000 + y)
        break
