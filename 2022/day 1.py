# part 1
print(max(sum(map(int,i.split())) for i in open("input.txt").read().split("\n\n")))

# part 2
print(sum(sorted(sum(map(int,i.split())) for i in open("input.txt").read().split("\n\n"))[-3:]))
