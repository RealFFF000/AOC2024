sum1 = 0
sum2 = 0
sum = 0
with open('input.txt') as input:
    # part 1
    lines = input.readlines()
    line = lines[0]
    line = line.split(" ")
    for number in range(len(line)):
        line[number] = [int(line[number]),1]
    print(line)
    for times in range(75):
        newline = []
        lastPercent = 0
        for number in range(len(line)): 
            if len(str(line[number][0]))%2 == 1:
                if line[number][0] == 0:
                    newline.append([1,line[number][1]])
                else:
                    newline.append([int(line[number][0])*2024,line[number][1]])
            else:
                newline.append([int(str(line[number][0])[:(len(str(line[number][0]))//2)]),line[number][1]])
                newline.append([int(str(line[number][0])[(len(str(line[number][0]))//2):]),line[number][1]])
        newline = sorted(newline,key=lambda x:x[0])
        line = newline
        del newline
        for number in range(len(line)):
            for otherNumber in range(number+1,len(line)):
                try:
                    if line[number][0] == line[otherNumber][0]:
                        line[number][1]+=line[otherNumber][1]
                        line.pop(otherNumber)
                except:
                    pass
        sum = 0
        for number in range(len(line)):
            sum+= line[number][1]
        print(times)
        if times == 24: sum1 = sum
    sum2 = sum
print(sum1,sum2)