import math

def checkDir(value,pos,grid,part2):
    x = pos[0]
    y = pos[1]
    leftVal = []
    rightVal = []
    upVal = []
    downVal = []
    for left in range(x-1,-1,-1):
        leftVal.append(int(grid[y][left]))
    for right in range(x+1,len(grid)):
        rightVal.append(int(grid[y][right]))
    for up in range(y-1,-1,-1):
        upVal.append(int(grid[up][x]))
    for down in range(y+1,len(grid)):
        downVal.append(int(grid[down][x]))
    if not part2:
        leftVis = True
        rightVis = True
        upVis = True
        downVis = True
        for v in leftVal:
            if v>=value:
                leftVis = False
                break
        for v in rightVal:
            if v>=value:
                rightVis = False
                break    
        for v in upVal:
            if v>=value:
                upVis = False
                break
        for v in downVal:
            if v>=value:
                downVis = False
                break
        return leftVis or rightVis or upVis or downVis
    if part2:
        leftScore = 0
        rightScore = 0
        upScore = 0
        downScore = 0
        for v in leftVal:
            if v>=value:
                leftScore+=1
                break
            elif v<value:
                leftScore+=1
        for v in rightVal:
            if v>=value:
                rightScore+=1
                break
            elif v<value:
                rightScore+=1
        for v in upVal:
            if v>=value:
                upScore+=1
                break
            elif v<value:
                upScore+=1
        for v in downVal:
            if v>=value:
                downScore+=1
                break
            elif v<value:
                downScore+=1
        return leftScore*rightScore*upScore*downScore
                

file = open("Day8/day8.txt",'r')
#file = open("Day8/day8test.txt",'r')

grid = []
for line in file:
    line = line.strip()
    grid.append(line)

total = len(grid)*4 - 4
#grid[y][x]

#Part 1
for y in range(1,len(grid)-1):
    for x in range(1,len(grid[0])-1):
        vis = checkDir(int(grid[y][x]),(x,y),grid,False)
        if vis:
            total += 1
print(total)

#Part 2
highest = 0
for y in range(1,len(grid)-1):
    for x in range(1,len(grid[0])-1):
        val = checkDir(int(grid[y][x]),(x,y),grid,True)
        if val > highest:
            highest = val
print(highest)
