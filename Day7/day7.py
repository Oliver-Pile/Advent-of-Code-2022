import string
class Tree():
    def __init__(self, name,parent):
        self.name = name
        self.children = []
        self.files = {}
        self.parent = parent
        
allNodes = []  
        
#Gets all the file values in the directory only, doesn't go into indirect files
def search(dirs,total):
    if len(dirs) != 0:
        for d in dirs:
            total = search(d.children,total)
            sum = 0
            for f in d.files.keys():
                sum += int(f)
            if sum<100000:
                total += sum
        return total
    else:
        return total

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

    
    
#file = open("Day7/day7.txt")
file = open("Day7/day7test.txt",'r')

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

vals = {}
for n in allNodes:
    val = newSearch(n)
    vals.update({n.name:val})
total = 0
print(vals)
for v in vals.values():
    if v<100000:
        total += v

print(total)
# print("Yay?")
                