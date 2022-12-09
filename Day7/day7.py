import string, math
class Tree():
    def __init__(self, name,parent):
        self.name = name
        self.children = []
        self.files = {}
        self.parent = parent
        
allNodes = []  

def getNodes(node,list):
    children = node.children
    for c in children:
        list = getNodes(c,list)
        list.append(c)
    return list


def newSearch(node):
    toCheck = getNodes(node,[node])
    total = 0
    for n in toCheck:
        for f in n.files.keys():
            total += int(f)
    return total

    
    
file = open("Day7/day7.txt")

root = Tree("/",None)
currentNode = root
for line in file:
    line = line.replace("\n","")
    if(line[0:4] == "$ cd"):
        path = line[5:].strip()
        if(path == ".."):
            currentNode = currentNode.parent
        elif(path == "/"):
            continue
        else:
            for t in currentNode.children:
                if t.name == path:
                    currentNode = t
                    break
    elif(line[0]!= "$"):
        if(line[0:3] == "dir"):
            dirName = line[4:].strip()
            exists = False
            for c in currentNode.children:
                if c.name == dirName:
                    exists = True
                    break
            if not exists:
                newNode = Tree(dirName,currentNode)
                allNodes.append(newNode)
                currentNode.children.append(newNode)
        elif(line[0] in string.digits):
            splitFile = line.split(" ")
            if splitFile[1] not in currentNode.files.values():
                currentNode.files.update({splitFile[0]:splitFile[1]})

vals = []
for n in allNodes:
    val = newSearch(n)
    vals.append(val)
total = 0
for v in vals:
    if v<100000:
        total += v
print(total)

#For part 2
rootSpace = newSearch(root)
unused = 70000000-rootSpace
remaining = 30000000 - unused
smallest = math.inf
for v in vals:
    if v>remaining:
        if v<smallest:
            smallest = v
print(smallest)
                