import string

def part1():
    file = open("Day3\day3.txt",'r')
    total =0
    for line in file:
        line = line.strip()
        mid = int(len(line)/2)
        com1 = line[:mid]
        com2 = line[mid:]
        for c in com1:
            if c in com2:
                if c in string.ascii_uppercase:
                    total += (ord(c)-38)
                if c in string.ascii_lowercase:
                    total += (ord(c)-96)
                break
    print(total)

def part2():
    file = open("Day3\day3.txt",'r')
    total = 0
    i = 0
    group = ["","",""]
    for line in file:
        line = line.strip()
        group[i] = line
        if i ==2:
            i = 0
            for c in group[0]:
                if c in group[1] and c in group[2]:
                    if c in string.ascii_uppercase:
                        total += (ord(c)-38)
                    elif c in string.ascii_lowercase:
                        total += (ord(c)-96)
                    break
        else:
            i+=1
    print(total)

part1()
part2()



