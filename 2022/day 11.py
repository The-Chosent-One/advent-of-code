# Learning about modular arithmetic !

# part 1
import re
from typing import Callable

monkey_input = open("input.txt").read()
information = re.findall(r"Starting items: (.+)+\n.+new = (.+)\n.+?(\d+)\n.+?(\d+)\n.+?(\d+)", monkey_input)
monkeys = []

class Monkey:
    def __init__(self, items: list[int], operation: Callable[[int], int], test: int, positive: int, negative: int) -> None:
        self.items = items
        self.operation = operation
        self.next_monkey = lambda w: [negative, positive][w % test == 0]
        self.count = 0

    def shenanigans(self):
        self.items = [*map(self.operation, self.items)]
        self.count += len(self.items)

for items, operation, test, positive, negative in information:
    items = eval(f"[{items}]")
    operation = eval(f"lambda old:({operation})//3")
    test, positive, negative = map(int, (test, positive, negative))

    monkeys.append(Monkey(items, operation, test, positive, negative))

for _ in range(20):
    for m in monkeys:
        m.shenanigans()
        for item in m.items:
            monkeys[m.next_monkey(item)].items.append(item)
        
        m.items = []

req = sorted([m.count for m in monkeys])[-2:]
print(req[0]*req[1])

# part 2

mods = [int(i[2]) for i in information]
monkeys = []

class MonkeyNumber:
    def __init__(self, num: int | dict) -> None:
        if isinstance(num, int):
            self.num = {m: num % m for m in mods}
        if isinstance(num, dict):
            self.num = num
    
    def __repr__(self) -> str:
        return str(self.num)

    def __add__(self, other: int):
        return MonkeyNumber({m: (n+other) % m for m,n in self.num.items()})
    
    def __radd__(self, other: int):
        return MonkeyNumber({m: (n+other) % m for m,n in self.num.items()})
    
    def __mul__(self, other):
        if isinstance(other, MonkeyNumber):
            return self.exponentiate(2)
        return MonkeyNumber({m: (n*other) % m for m,n in self.num.items()})

    def __rmul__(self, other):
        if isinstance(other, MonkeyNumber):
            return self.exponentiate(2)
        return MonkeyNumber({m: (n*other) % m for m,n in self.num.items()})
        
    def exponentiate(self, num: int):
        # we'll only ever use num=2 but why not
        return MonkeyNumber({m: (n**num) % m for m,n in self.num.items()})

class Monkey2:
    def __init__(self, items: list[MonkeyNumber], operation: Callable[[MonkeyNumber], int], test: int, positive: int, negative: int) -> None:
        self.items = items
        self.operation = operation
        self.next_monkey = lambda monkeynum: [negative, positive][monkeynum.num[test] == 0]
        self.count = 0

    def shenanigans(self):
        self.items = [*map(self.operation, self.items)]
        self.count += len(self.items)

for items, operation, test, positive, negative in information:
    items = [*map(MonkeyNumber, eval(f"[{items}]"))]
    operation = eval(f"lambda old:({operation})")
    test, positive, negative = map(int, (test, positive, negative))

    monkeys.append(Monkey2(items, operation, test, positive, negative))

for _ in range(10000):
    for m in monkeys:
        m.shenanigans()
        for item in m.items:
            monkeys[m.next_monkey(item)].items.append(item)
        
        m.items = []

req = sorted([m.count for m in monkeys])[-2:]
print(req[0]*req[1])
