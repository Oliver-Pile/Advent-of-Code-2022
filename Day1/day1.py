file = open("Day1/day1.txt","r")
values = []
total = 0
largest = 0
for line in file:
    if(line=="\n"):
        values.append(total)
        total = 0
    else:
        line = line.strip()
        total += int(line)

values.sort(reverse=True)
print("Part 1: ",values[0])
print("Part 2: ",values[0]+values[1]+values[2])
