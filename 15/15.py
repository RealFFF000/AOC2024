sum1 = 0
sum2 = 0
directionsSigns = ["^",">","v","<"]
directions = [[-1,0],[0,1],[1,0],[0,-1]]

def move(Y,X,directionSign):
    direction = directions[directionsSigns.index(directionSign)]
    selfCharacter = map[Y][X]
    characterInWay = map[Y+direction[0]][X+direction[1]]
    if characterInWay == "O":
        move(Y+direction[0],X+direction[1],directionSign)
    characterInWay = map[Y+direction[0]][X+direction[1]]
    if characterInWay == ".":
        map[Y+direction[0]][X+direction[1]] = selfCharacter
        map[Y][X] = "."

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

    
    for instruction in instructions:
        robotX = 0
        robotY = 0
        for line in range(len(map)):
            for character in range(len(map[line])):
                if map[line][character] == "@":
                    robotX = character
                    robotY = line
        move(robotY,robotX,instruction)
        print(instruction)
        for line in range(len(map)):
            for character in map[line]:
                print(character,end="")
            print("")
    for line in range(len(map)):
        for character in range(len(map[line])):
            if map[line][character] == "O":
                sum1+=((100*line)+character)
    print(sum1)