sum1Help = []
sum1 = 0
sum2 = 0
directions = [[-1,0],[0,1],[1,0],[0,-1]]

def checkSurround(line,character,depth):
    if depth == 9:
        if [line,character] not in sum1Help:
            sum1Help.append([line,character])
        return 1
    didsomething = False
    for rotation in directions:
        if line+rotation[0]>=0 and line+rotation[0]<len(lines) and character+rotation[1]>=0 and character+rotation[1]<len(lines[line]): 
            if int(lines[line+rotation[0]][character+rotation[1]]) == (depth+1):
                didsomething = True
                print("found",depth+1,"in",line+rotation[0],character+rotation[1])
                checkSurround(int(line+rotation[0]),int(character+rotation[1]),depth+1)
    if not didsomething:
        return 0
with open('input.txt') as input:
    # part 1
    lines = input.readlines()
    for line in range(len(lines)):
        if lines[line][-1] == "\n":
            lines[line] = lines[line][:-1]
    
    for line in range(len(lines)):
        for character in range(len(lines[line])):
            if int(lines[line][character]) == 0:
                print("found 0 in",line,character)
                checkSurround(line,character,0)
                sum1 += len(sum1Help)
                sum1Help = []
print(sum1, sum2)