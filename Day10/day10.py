def getSprite(x,pos):
    return pos in [x-1,x,x+1]

file = open("Day10/day10.txt",'r')
#file = open("Day10/day10test.txt",'r')

cycle = 0
allCycles = {}
crt=[]
x = 1
for line in file:
    if line[0:4] == 'noop':
        cycle += 1
        if getSprite(x,(len(crt)%40)):
            crt.append("#")
        else: crt.append(".")
        allCycles.update({cycle:x})
    else:
        for c in range(2):
            cycle+=1
            if getSprite(x,(len(crt)%40)):
                crt.append("#")
            else: crt.append(".")
            allCycles.update({cycle:x})
        val = int(line.split()[1])
        x += val
print((allCycles[20]*20)+(allCycles[60]*60)+(allCycles[100]*100)+(allCycles[140]*140)+(allCycles[180]*180)+(allCycles[220]*220))
crtStr = "".join(crt)
print(crtStr[0:40])
print(crtStr[40:80])
print(crtStr[80:120])
print(crtStr[120:160])
print(crtStr[160:200])
print(crtStr[200:240])
