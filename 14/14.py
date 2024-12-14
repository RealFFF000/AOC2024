import re
q1= 0
q2 = 0
q3 = 0
q4 = 0
width = 101
height = 103
time = 100
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

    for robot in range(len(data)):
        finalX = (data[robot][0]+(time*data[robot][2]))%width
        finalY = (data[robot][1]+(time*data[robot][3]))%height
        print(finalX,finalY)

        if finalX>(width//2):
            if finalY>(height//2):
                q1+=1
            if finalY<(height//2):
                q2+=1
        if finalX<(width//2):
            if finalY>(height//2):
                q3+=1
            if finalY<(height//2):
                q4+=1
    print(q1*q2*q3*q4)
    #print(data)