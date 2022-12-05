import string
def day5(part2):
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
    for ins in instructions:
        splitIns = ins.strip().split(" ")
        if (not part2):
            for _ in range(int(splitIns[1])):
                crate = allStacks[int(splitIns[3])-1].pop()
                allStacks[int(splitIns[5])-1].append(crate)
        else:
            crates = []
            for _ in range(int(splitIns[1])):
                crates.append(allStacks[int(splitIns[3])-1].pop())
            for _ in range(len(crates)):
                allStacks[int(splitIns[5])-1].append(crates.pop())

    tops = []
    for s in allStacks:
        tops.append(s[-1])
    print("".join(tops))


day5(False)
day5(True)

