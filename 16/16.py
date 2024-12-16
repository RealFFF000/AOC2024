import sys
sys.setrecursionlimit(10000000)
sum1 = 0
sum2 = 0
directions = [[-1,0],[0,1],[1,0],[0,-1]]
stack = []
scores = []
def printMap(lines,map):
    for Y in range(len(lines)):
        for X in range(len(lines[Y])):
            if [Y,X] in map:
                print("A",end="")
            else:
                print(lines[Y][X],end="")
        print("")
def go(Y,X):
    stack.append([])
    for direction in directions:
        if lines[Y+direction[0]][X+direction[1]] == ".":
            stack[-1] = [Y,X]
            if [Y+direction[0],X+direction[1]] not in stack:
                go(Y+direction[0],X+direction[1])
        if lines[Y+direction[0]][X+direction[1]] == "E":
            stack[-1] = [Y,X]
            lastDirection = [stack[1][0]-stack[0][0],stack[1][1]-stack[0][1]]
            tempScore = 1000
            for spot in range(len(stack)-1):
                currentDirection = [stack[spot+1][0]-stack[spot][0],stack[spot+1][1]-stack[spot][1]]
                if currentDirection != lastDirection:
                    tempScore+=1000
                    lastDirection = currentDirection
            print(len(stack)+tempScore)
            printMap(lines,stack)
            scores.append(len(stack)+tempScore)
    del stack[-1]

with open('input.txt') as input:
    # part 1 and 2
    lines = input.readlines()
    for line in range(len(lines)):
        lines[line] = lines[line].replace("\n","")
        for character in range(len(lines[line])):
            if lines[line][character] == "S":
                go(line,character)
    lowestScore = 0
    for score in scores:
        if lowestScore == 0:
            lowestScore = score
        else:
            if lowestScore>score:
                lowestScore = score
    print("\n",lowestScore)