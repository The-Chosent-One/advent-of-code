# part 1
print(sum((s:=({*l[len(l)//2:]}&{*l[:len(l)//2]}).pop(),ord(s)-38-(ord(s)-96>0)*58)[1]for l in open("input.txt").read().split()))

# part 2
print(sum((v:=s.pop(),ord(v)-38-(ord(v)-96>0)*58)[1]for i,l in enumerate(open("input.txt").read().split(),1)if((i-1)%3<1 and(s:={*l}),s:=s&{*l},i%3<1)[2]))
