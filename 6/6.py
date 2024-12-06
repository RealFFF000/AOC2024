sum1 = 0
sum2 = 0

def rotate(direction):
    if direction == [-1,0]: direction = [0,1]
    elif direction == [0,1]: direction = [1,0]
    elif direction == [1,0]: direction = [0,-1]
    elif direction == [0,-1]: direction = [-1,0]
    return direction

def visualise(lines,obstacle,visited):
    for line in range(len(lines)):
        for character in range(len(lines[line])):
            if [obstacle[0],obstacle[1]] == [line,character]:
                print("O",end="")
            elif [line,character] in visited:
                print("*",end="")
            else:
                print(lines[line][character],end="")
with open('input.txt') as input:
    # part 1
    lines = input.readlines()

    guardXsave,guardYsave = 0,0
    for Y in range(len(lines)):
        for X in range(len(lines[Y])):
            if lines[Y][X] == "^":
                guardXsave,guardYsave = X,Y
        lines[Y].replace("\n","")
    visited = []
    for generation in range(0,4515):
        #print(generation)
        guardX,guardY = guardXsave,guardYsave
        direction = [-1,0]
        visitedThisGen = []
        if generation != 0:
            obstacle = visited[generation]
            #print(visited)
        else:
            obstacle = [-1,-1]
        step = 0
        backtracedSteps = 0
        while True:
            step += 1
            if backtracedSteps > 100:
                print("loop found",generation)
                sum2+=1
                #visualise(lines,obstacle,visited)
                break
                ([guardY,guardX])
            elif guardX+direction[1] in range(len(lines[0])) and guardY+direction[0] in range(len(lines)):

                #print(obstacle)
                if lines[guardY+direction[0]][guardX+direction[1]] == "#" or [guardY+direction[0],guardX+direction[1]] == obstacle:
                    direction = rotate(direction)
                else:
                    guardX += direction[1]
                    guardY += direction[0]

                    if generation == 0:
                        if [guardY,guardX] in visited:
                            pass
                        else:
                            sum1 += 1
                            visited.append([guardY,guardX])

                    if [guardY,guardX] in visitedThisGen:
                        backtracedSteps += 1
                    else:
                        visitedThisGen.append([guardY,guardX])
                        backtracedSteps = 0
            else:
                #visualise(lines,obstacle,visited)
                break

    
print(sum1,sum2-1)