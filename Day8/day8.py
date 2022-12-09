def checkDir(value,pos,grid):
    vis = True
    x = pos[0]
    y = pos[1]
    for left in range(x,-1):
        if grid[y][left] > value:
            vis = False
            break
    for right in range(x,len(grid)):
        if grid[y][right] > value:
            vis = False
    for up in range(y,-1):
        if grid[up][x] > value:
            vis = False
    for down in range(y,len(grid)):
        if grid[down][x] > value:
            vis = False
    return vis

# file = open("Day8/day8.txt",'r')
file = open("Day8/day8test.txt",'r')

grid = []
for line in file:
    line = line.strip()
    grid.append(line)

total = len(grid)*4 - 4
#grid[y][x]

for y in range(1,len(grid)):
    for x in range(1,len(grid[0])):
        vis = checkDir(grid[y][x],(x,y),grid)
        if vis:
            total += 1

print(total)
