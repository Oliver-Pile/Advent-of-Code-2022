def day4(day2=False):
    file = open("Day4\day4..txt",'r')
    numbers = list(range(0,100))
    total = 0
    for line in file:
        splitLine = line.strip().split(",")
        pair1 = splitLine[0].split("-")
        pair2 = splitLine[1].split("-")
        job1 = set(numbers[int(pair1[0]):int(pair1[1])+1])
        job2 = set(numbers[int(pair2[0]):int(pair2[1])+1])
        if(not day2):
            if(job1.issubset(job2) or job2.issubset(job1)):
                total += 1
        else:
            if(len(job1.intersection(job2)) >0):
                total +=1
    return total
    
print(day4())
print(day4(True))



