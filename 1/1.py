sum1 = 0
sum2 = 0
with open('input.txt') as input:
    #part 1 

    lines = input.readlines()

    leftCollumn = []
    rightCollumn = []
    for line in lines:
        leftCollumn.append(int(line.split(" ")[0]))
        rightCollumn.append(int(line.split(" ")[-1].replace("\n","")))

    leftCollumn.sort()
    rightCollumn.sort()

    for line in range(len(lines)):
        sum1 += abs((leftCollumn[line] - rightCollumn[line]))

    #part 2
    for line in range(len(lines)):
        number = leftCollumn[line]
        appearences = rightCollumn.count(number)
        sum2 += (appearences*number)


print(sum1,sum2)
