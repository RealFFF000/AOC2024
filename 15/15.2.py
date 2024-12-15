sum1 = 0
sum2 = 0
directionsSigns = ["^",">","v","<"]
directions = [[-1,0],[0,1],[1,0],[0,-1]]

def movable(Y,X,directionSign):
    direction = directions[directionsSigns.index(directionSign)]
    if biggerMap[Y+direction[0]][X+direction[1]] == "[":
        return (movable(Y+direction[0],X+direction[1],directionSign) and movable(Y+direction[0],X+1+direction[1],directionSign)) 
    elif biggerMap[Y+direction[0]][X+direction[1]] == "]":
        return (movable(Y+direction[0],X+direction[1],directionSign) and movable(Y+direction[0],(X-1)+direction[1],directionSign)) 
    elif biggerMap[Y+direction[0]][X+direction[1]] == ".":
        return True
    elif biggerMap[Y+direction[0]][X+direction[1]] == "#":
        return False
def move(Y,X,directionSign):
    direction = directions[directionsSigns.index(directionSign)]
    selfCharacter = biggerMap[Y][X]
    characterInWay = biggerMap[Y+direction[0]][X+direction[1]]
    if direction == [-1,0] or direction == [1,0]:
        if movable(Y,X,directionSign):
            if biggerMap[Y+direction[0]][X+direction[1]] == "[":
                move(Y+direction[0],X+direction[1],directionSign)
                move(Y+direction[0],X+1+direction[1],directionSign)
            if biggerMap[Y+direction[0]][X+direction[1]] == "]":
                move(Y+direction[0],X+direction[1],directionSign)
                move(Y+direction[0],X-1+direction[1],directionSign)
    else:
        if characterInWay == "[" or characterInWay == "]":
            move(Y+direction[0],X+direction[1],directionSign)
    characterInWay = biggerMap[Y+direction[0]][X+direction[1]]
    if characterInWay == ".":
        biggerMap[Y+direction[0]][X+direction[1]] = selfCharacter
        biggerMap[Y][X] = "."

with open('input.txt') as input:
    # part 1 and 2
    map = []
    lines = input.readlines()
    instructions = lines[-1]
    for line in range(len(lines)-2):
        map.append([])
    for line in range(len(map)):
        for character in range(len(lines[line])):
            if lines[line][character]!="\n":
                map[line].append(lines[line][character])
        print(map[line])
    print(instructions)
    biggerMap = []
    for line in range(len(map)):
        biggerMap.append([])
        for character in range(len(map[line])):
            if map[line][character] == "#":
                biggerMap[line].append("#")
                biggerMap[line].append("#")
            elif map[line][character] == "O":
                biggerMap[line].append("[")
                biggerMap[line].append("]")
            elif map[line][character] == "@":
                biggerMap[line].append("@")
                biggerMap[line].append(".")
            elif map[line][character] == ".":
                biggerMap[line].append(".")
                biggerMap[line].append(".")
    
    for instruction in instructions:
        robotX = 0
        robotY = 0
        for line in range(len(biggerMap)):
            for character in range(len(biggerMap[line])):
                if biggerMap[line][character] == "@":
                    robotX = character
                    robotY = line
        move(robotY,robotX,instruction)
        print(instruction)

    for line in range(len(biggerMap)):
        for character in biggerMap[line]:
            print(character,end="")
        print("")
    
    for line in range(len(biggerMap)):
        for character in range(len(biggerMap[line])):
            if biggerMap[line][character] == "[":
                sum1+=((100*line)+character)
    
    print(sum1)