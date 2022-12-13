# part 1
unparsed_pairs = open("input.txt").read().split("\n\n")
pairs = [[eval(l) for l in p.split()] for p in unparsed_pairs]
correct = 0

def correct_input(first: list | int, second: list | int) -> bool | None:
    if isinstance(first, list) and isinstance(second, int):
        return correct_input(first, [second])

    if isinstance(first, int) and isinstance(second, list):
        return correct_input([first], second)

    if all(isinstance(i, int) for i in [first, second]):
        return None if first == second else first < second

    if all(isinstance(i, list) for i in [first, second]):
        for f, l in zip(first, second):
            res = correct_input(f, l)
            if res is None:
                continue
            return res
        
        return None if len(first) == len(second) else len(first) < len(second)

for index, (first, second) in enumerate(pairs, 1):
    correct += correct_input(first, second) * index

print(correct)

# part 2
unparsed_lists = open("input.txt").read().split()
# a very specific implementation for a list
class SpecificList:
    def __init__(self, _underlying: list) -> None:
        self._underlying = _underlying
    
    def __lt__(self, other):
        return correct_input(self._underlying, other._underlying)

lists = [SpecificList(eval(l)) for l in unparsed_lists] + [SpecificList(l) for l in [[[2]], [[6]]]]
sorted_lists = [[]] + [sl._underlying for sl in sorted(lists)]

print(sorted_lists.index([[2]])*sorted_lists.index([[6]]))
