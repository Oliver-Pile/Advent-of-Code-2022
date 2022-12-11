import math

def nextTo(headPos, tailPos):
    return (abs(headPos[0] - tailPos[0]) in [0,1] and abs(headPos[1] - tailPos[1]) in [0,1])

def surrounding(pos):
    x,y = pos
    return [[x-1,y-1],[x,y-1],[x+1,y-1],[x-1,y],[x+1,y],[x-1,y+1],[x,y+1],[x+1,y+1]]

def intersection(listA,listB):
    both = []
    for x in listA:
        if x in listB:
            both.append(x)
    return both

#Get next to new head
#Get all valid tail moves
#Get intersection then move their
#Set head move to single at a time.
#Try for horiz first

file = open("Day9\day9.txt",'r')
#file = open("Day9\day9test.txt",'r')

visited = [[0,0]]
headPos = [0,0]
tailPos = [0,0]
for line in file:
    dir,val = line.split()
    for v in range(int(val)):
        if dir == 'L':
            headPos[0] -= 1
        if dir == 'R':
            headPos[0] += 1
        if dir == 'U':
            headPos[1] += 1
        if dir == 'D':
            headPos[1] -= 1
        tailnext = nextTo(headPos,tailPos)
        if not tailnext:
            validHead = surrounding(headPos)
            validTail = surrounding(tailPos)
            samePos = intersection(validHead,validTail)
            sameHoriz = []
            for s in samePos:
                x,y = s
                if x == headPos[0] or y == headPos[1]:
                    sameHoriz.append(s)
            if len(sameHoriz)==1:
                tailPos=sameHoriz[0]
            else:
                tailPos=samePos[0]
            if tailPos not in visited:
                visited.append(tailPos)
print(len(visited))