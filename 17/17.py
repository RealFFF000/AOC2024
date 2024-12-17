import re
A = 0
B = 0
C = 0
instructions = []


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
    print(Argument%8,end=",")


with open('input.txt') as input:
    lines = input.readlines()
    index = 0
    for line in lines:
        if re.findall(r'[\d]+',line) == []:
            pass
        else:
            if index == 0:
                A = int(re.findall(r'[\d]+',line)[0])
            elif index == 1:
                B = int(re.findall(r'[\d]+',line)[0])
            elif index == 2:
                C = int(re.findall(r'[\d]+',line)[0])
            elif index == len(lines)-1:
                instructions = re.findall(r'[\d]+',line) 
        index+=1
    for instruction in range(len(instructions)):
        instructions[instruction] = int(instructions[instruction])
    print(A,B,C,instructions,sep="\n")
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