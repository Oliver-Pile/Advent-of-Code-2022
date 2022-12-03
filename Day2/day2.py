# X/A Rock
# Y/B Paper
# Z/C Scissors

loose = {
    'B':'X',
    'C':'Y',
    'A':'Z'
}
draw = {
    'A':'X',
    'B':'Y',
    'C':'Z'
}
win = {
    'C':'X',
    'A':'Y',
    'B':'Z'
}
points = {
    'X':1,
    'Y':2,
    'Z':3
}

def part1():
    file = open("Advent-of-Code-2022\Day2\day2.txt","r")
    total = 0
    for line in file:
        split = line.strip().split(" ")
        other = split[0]
        hand = split[1]
        total += points[hand]
        if draw[other] == hand:
            total += 3
        elif win[other] == hand:
            total += 6
    print(total)

def part2():
    file = open("Advent-of-Code-2022\Day2\day2.txt","r")
    total = 0
    for line in file:
        split = line.strip().split(" ")
        other = split[0]
        outcome = split[1]
        if outcome == 'X':
            total += points[loose[other]]
        elif outcome == 'Y':
            total += 3 + points[draw[other]]
        else:
            total += 6 + points[win[other]]
    print(total)

part1()   
part2()

        

