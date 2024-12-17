import re
A = 0
B = 0
C = 0
instructions = []
sum = []

def combo(X,A,B,C):
    if X in range(0,4):
        return X
    if X == 4:
        return A
    if X == 5:
        return B
    if X == 6:
        return C
def adv(A,Argument):
    return A//(2**Argument)
def bxl(B,Argument):
    return B ^ Argument
def bst(Argument):
    return Argument%8
def jnz(A,Argument):
    return (A == 0)
def bxc(B,C):
    return B ^ C
def out(Argument):
    sum.append(Argument%8)
    #print(Argument%8,end=",")


with open('input.txt') as input:
    lines = input.readlines()
    index = 0
    for line in lines:
        if re.findall(r'[\d]+',line) == []:
            pass
        else:
            if index == 0:
                A = 0
            elif index == 1:
                B = int(re.findall(r'[\d]+',line)[0])
            elif index == 2:
                C = int(re.findall(r'[\d]+',line)[0])
            elif index == len(lines)-1:
                instructions = re.findall(r'[\d]+',line) 
        index+=1
    for instruction in range(len(instructions)):
        instructions[instruction] = int(instructions[instruction])
    number = 10
    while True:
        sum = []
        A = number
        #print(A,instructions,sep="\n")
        instruction = 0
        while instruction < len(instructions)-1:
            ignore = False
            #print(A,B,C,"\n",instructions[instruction], instructions[instruction+1])
            if instructions[instruction] == 0:
                A = adv(A,combo(instructions[instruction+1],A,B,C))
            elif instructions[instruction] == 1:
                B = bxl(B,instructions[instruction+1])
            elif instructions[instruction] == 2:
                B = bst(combo(instructions[instruction+1],A,B,C))
            elif instructions[instruction] == 3:
                if A != 0:
                    ignore = True
            elif instructions[instruction] == 4:
                B = bxc(B,C)
            elif instructions[instruction] == 5:
                out(combo(instructions[instruction+1],A,B,C))
            elif instructions[instruction] == 6:
                B = adv(A,combo(instructions[instruction+1],A,B,C))
            elif instructions[instruction] == 7:
                C = adv(A,combo(instructions[instruction+1],A,B,C))
            if not ignore:
                instruction += 2
            else:
                instruction = instructions[instruction+1]
        print(number)
        print(sum,instructions,sep="\n")
        if sum == instructions:
            break
        if len(sum) < len(instructions):
            number = int(number*1.2)
        elif sum[-1] != instructions[-1]:
            number = int(number*1.1)
        elif sum[-2] != instructions[-2]:
            number = int(number*1.01)
        elif sum[-3] != instructions[-3] or sum[-4] != instructions[-4]:
            number +== int(number*1.000001)
        elif sum[-6] != instructions[-6] or sum[-7] != instructions[-7] or sum[-5] != instructions[-5]:
            number = int(number*1.00000001)
        elif sum[-9] != instructions[-9]:
            number = int(number*1.000000000001)
        elif sum[-10] != instructions[-10]:
            number = int(number*1.0000000000001)
        elif sum[-11] != instructions[-11]:
            number = int(number*1.00000000000001)
        else:
            number+=1
        #not elegant, but working