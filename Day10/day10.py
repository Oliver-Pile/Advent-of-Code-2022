file = open("Day10/day10.txt",'r')

cycle = 0
allCycles = {}
x = 1
for line in file:
    if line[0:4] == 'noop':
        cycle += 1
        allCycles.update({cycle:x})
    else:
        for c in range(2):
            cycle+=1
            allCycles.update({cycle:x})
        val = int(line.split()[1])
        x += val
print((allCycles[20]*20)+(allCycles[60]*60)+(allCycles[100]*100)+(allCycles[140]*140)+(allCycles[180]*180)+(allCycles[220]*220))
