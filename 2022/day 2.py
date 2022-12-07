# part 1
print(sum(ord(b)-87+[3,6,0][ord(b)-ord(a)-23]for a,_,b in open("input.txt").read().split("\n")))

# part 2
print(sum(3*ord(b)-263+(ord(a)+ord(b)-154)%3 for a,_,b in open("input.txt").read().split("\n")))
