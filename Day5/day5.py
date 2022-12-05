import string
file = open("Day5/day5.txt",'r')

allStacks = []
l = file.readlines()
splitIndex = l.index('\n')
stacks = list(reversed(l[:splitIndex-1]))
instructions = l[splitIndex+1:]
for x in range(9):
    allStacks.append(list())
for r in stacks:
    r = r[:-2]
    for i,c in enumerate(r):
        if(c in string.ascii_uppercase):
            allStacks[int(i/4)].append(c)
        
print("x")

