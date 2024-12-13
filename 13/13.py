import re
bigNumber = 10000000000000
def calculate(offset,data):
    sum=0
    for machine in data:
        
        p_x = machine[2][0]+offset
        p_y = machine[2][1]+offset
        a_x = machine[0][0]
        a_y = machine[0][1]
        b_x = machine[1][0]
        b_y = machine[1][1]

        A = round((p_y - ((b_y * p_x) / b_x)) / (a_y - ((b_y * a_x) / b_x)))
        B = round((p_x - a_x * A) / b_x)
        if int(B) == B:
            if a_x * A + b_x * B == p_x and a_y * A + b_y * B == p_y:
                sum += A * 3 + B
    print(sum)

with open('input.txt') as input:
    # part 1 and 2
    data = [[]]
    lines = input.readlines()
    index = 0
    for line in lines:
        if re.findall(r'[\d]+',line) == []:
            data.append([])
            index+=1
        else:
            data[index].append(re.findall(r'[\d]+',line))
            for number in range(len(data[index][-1])):
                data[index][-1][number] = int(data[index][-1][number])

    calculate(0,data)
    calculate(bigNumber,data)