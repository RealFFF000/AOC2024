import re

width = 101
height = 103
finalData = []


with open('input.txt') as input:
    # part 1 and 2
    data = []
    lines = input.readlines()
    index = 0
    for line in lines:
        data.append(re.findall(r'-?\d+',line))
    for robot in range(len(data)):
        for number in range(len(data[robot])):
            data[robot][number] = int(data[robot][number])
    with open("output.txt", "a") as f:
        for time in range(0,10000):
            print("_____________________________",file=f)
            print(time,file=f)
            finalData = []
            for robot in range(len(data)):
                finalX = (data[robot][0]+(time*data[robot][2]))%width
                finalY = (data[robot][1]+(time*data[robot][3]))%height
                finalData.append([finalX,finalY])
            for a in range(height):
                for b in range(width):
                    if [b,a] in finalData:
                        print("*",end="",file=f)
                    else:
                        print(" ",end="",file=f)
                print("",file=f)