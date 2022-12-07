import string
class Tree():
    def __init__(self, name,parent):
        self.name = name
        self.children = []
        self.files = {}
        self.parent = parent
        

def search(dirs,total):
    if len(dirs) != 0:
        for d in dirs:
            total = search(d.children,total)
            sum = 0
            for f in d.files.keys():
                sum += int(f)
            if sum <100000:
                total += sum
        return total
    else:
        return total
    
#file = open("Day7\day7.txt")
file = open("Day7\day7test.txt",'r')

root = Tree("/",None)
currentNode = root
for line in file:
    line = line[:-1]
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
                currentNode.children.append(Tree(dirName,currentNode))
        elif(line[0] in string.digits):
            splitFile = line.split(" ")
            if splitFile[1] not in currentNode.files.values():
                currentNode.files.update({splitFile[0]:splitFile[1]})

           
total = search(root.children,0)
print(total)
print("Yay?")
                