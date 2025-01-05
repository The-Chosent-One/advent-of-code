from collections import defaultdict, deque

with open("input.txt", "r") as file:
    initial_secrets = [*map(int, file.read().split("\n"))]

def get_secret(secret: int):
    yield secret
    for _ in range(2000):
        secret = (secret ^ (secret << 6)) & 16777215
        secret = (secret ^ (secret >> 5)) & 16777215
        secret = (secret ^ (secret << 11)) & 16777215
        yield secret

part1 = 0
master = defaultdict(int)

for secret in initial_secrets:
    secret_generator = get_secret(secret)
    past = deque(maxlen=5)

    for _ in range(4):
        past.append(next(secret_generator) % 10)
    
    seen = set()

    for secret in secret_generator:
        price = secret % 10
        past.append(price)

        diff = tuple(past[i]-past[i-1] for i in range(1,5))
        if diff not in seen:
            master[diff] += price
        
        seen.add(diff)
        pass

    part1 += secret

optimal_diff, part2 = max(master.items(), key=lambda i:i[1])
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
