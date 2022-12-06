def day6(length):
    file = open("Day6/day6.txt",'r')
    input = file.read().strip()
    i=0
    while(i<len(input)+length):
        sub = set(input[i:i+length])
        if len(sub) == length:
            return i+length
        i+=1
print(day6(4))
print(day6(14))