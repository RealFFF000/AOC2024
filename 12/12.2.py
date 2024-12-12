sum1 = 0
directions = [[-1,0],[0,1],[1,0],[0,-1]]
cornerSets = [
    [[-1,0],[0,1]],
    [[0,1],[1,0]],
    [[1,0],[0,-1]],
    [[0,-1],[-1,0]]
]
toDraw = 1
blockArea = [0]
blockCorners = [0]
map = []
def printMap():
    for line in map:
        for character in line:
            print(character,end="")
        print("")

def explore(y,x,characterToDrawWith):
    blockArea[0]+=1
    map[y][x] = characterToDrawWith
    for direction in directions:
        if y+direction[0]>=0 and (y+direction[0])<(len(lines)) and x+direction[1]>=0 and (x+direction[1])<(len(lines[y])):
            #print("comparing",lines[y+direction[0]][x+direction[1]],"with",lines[y][x])
            if lines[y+direction[0]][x+direction[1]] == lines[y][x] and map[y+direction[0]][x+direction[1]] == 0:
                explore(y+direction[0],x+direction[1],characterToDrawWith)
            if not lines[y+direction[0]][x+direction[1]] == lines[y][x]:
                pass
        else:
            pass
            #print("apparently",y+direction[0],x+direction[1],"is considrered out of bounds")
    #3 necessary conditions 
    #1: either this or this
    #** *#
    #*# ##
    left = 0
    right = 0
    opposite = 0
    for direction in range(len(directions)):
        if y+directions[direction][0]>=0 and y+directions[direction][0]<len(lines):
            left = line[y+directions[direction][0]][x] 
        else:
            left = 0
        if x+directions[direction+1][1]>=0 and x+directions[direction+1][1]<len(lines[line]):
            right = line[y][x+directions[direction+1][1]]
        else:
            right = 0
        if y+directions[direction][0]>=0 and y+directions[direction][0]<len(lines) and x+directions[direction+1][1]>=0 and x+directions[direction+1][1]<len(lines[line]):
            opposite = line[y+directions[direction][0]][x+directions[direction+1][1]]
        else:
            opposite = 0

    
with open('input.txt') as input:
    lines = input.readlines()
    for line in range(len(lines)):
        lines[line] = lines[line].replace("\n","")
        map.append([])
        for character in range(len(lines[line])):
            map[line].append(0)

    for line in range(len(lines)):
        for character in range(len(lines[line])):
            if map[line][character] == 0:
                #printMap()
                print("")
                blockArea = [0]
                blockCorners = [0]
                explore(line,character,toDraw)
                print(lines[line][character])
                print(blockArea[0],blockCorners[0])
                print(blockArea[0]*blockCorners[0])
                sum1+=(blockArea[0]*blockCorners[0])
                toDraw += 1
                if toDraw == 10: toDraw = 1

print(sum1)

