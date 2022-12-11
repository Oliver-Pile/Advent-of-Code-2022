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
def day9(part2):
    file = open("Day9\day9.txt",'r')
    #file = open("Day9\day9test.txt",'r')
    
    visited = [[0,0]]
    if part2:
       pos = {
        0:[0,0],
        1:[0,0],
        2:[0,0],
        3:[0,0],
        4:[0,0],
        5:[0,0],
        6:[0,0],
        7:[0,0],
        8:[0,0],
        9:[0,0]
    }
    else: 
        pos = {
            0:[0,0],
            1:[0,0]
        }
        
    for line in file:
        dir,val = line.split()
        for v in range(int(val)):
            if dir == 'L':
                pos[0][0] -= 1
            if dir == 'R':
                pos[0][0] += 1
            if dir == 'U':
                pos[0][1] += 1
            if dir == 'D':
                pos[0][1] -= 1
            for key,val in pos.items():
                if(key != len(pos)-1):
                    tailnext = nextTo(pos[key],pos[key+1])
                    if not tailnext:
                        validHead = surrounding(pos[key])
                        validTail = surrounding(pos[key+1])
                        samePos = intersection(validHead,validTail)
                        sameHoriz = []
                        for s in samePos:
                            x,y = s
                            if x == pos[key][0] or y == pos[key][1]:
                                sameHoriz.append(s)
                        if len(sameHoriz)==1:
                            pos[key+1]=sameHoriz[0]
                        else:
                            pos[key+1]=samePos[0]
                        if key+1 == len(pos)-1 and pos[key+1] not in visited:
                                visited.append(pos[key])
    print(len(visited))

day9(False)
        