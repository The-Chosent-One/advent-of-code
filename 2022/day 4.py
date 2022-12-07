# part 1
print(sum((s:=eval("-".join(i.split("-")[::-1])),s[0]*s[1]<1)[1]for i in open("input.txt").read().split()))

# part 2
import re;print(sum((n:=[*map(int,re.findall(r"\d+",i))],n[2]-n[1]<1 and n[0]-n[3]<1)[1]for i in open("input.txt").read().split()))
