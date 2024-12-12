sum1 = 0
sum2 = 0
characters = []
groupAmounts = []
uniqueGroupsLines = []
visited = []
directions = [[-1,0],[0,1],[1,0],[0,-1]]

def paint(line,character,string):
    initialString = str(lines[line][character])
    if uniqueGroupsLines[line][character] == []:
        uniqueGroupsLines[line][character] = string
    visited.append([line,character])
    for direction in directions:
        try:
            if lines[line+direction[0]][character+direction[1]] == initialString and [line+direction[0],character+direction[1]] not in visited:
                paint(line+direction[0],character+direction[1],string)
        except:
            pass
        
with open('input.txt') as input:
    # part 1
    # firstly, let's make every individual group of a character unique character
    # I'm gonna do this by filling every group with (character+group number) scheme
    lines = input.readlines()
    for line in range(len(lines)):
        lines[line] = lines[line].replace("\n","")
        uniqueGroupsLines.append([])
        for character in range(len(lines[line])):
            uniqueGroupsLines[line].append([])
    for line in range(len(lines)):
        for character in range(len(lines[line])):
            if len(lines[line][character]) == 1:
                if lines[line][character] not in characters and [line,character] not in visited:
                    characters.append(lines[line][character])

                    groupAmounts.append(0)
                else:
                    if uniqueGroupsLines[line][character] == []:
                        groupAmounts[characters.index(lines[line][character])]+=1
                        paint(line,character,str(lines[line][character])+str(groupAmounts[characters.index(lines[line][character])]))
                    
                
                #this block has not been filled yet
    for line in lines:
        print(line)
    for line in uniqueGroupsLines:
        print(line)
    print(characters,groupAmounts,sep="\n")
    
    charactersIncludingVariety = []
    amounts = []
    perimeters = []
    for line in range(len(uniqueGroupsLines)):
        for character in range(len(uniqueGroupsLines[line])):
            if uniqueGroupsLines[line][character] not in charactersIncludingVariety:
                charactersIncludingVariety.append(uniqueGroupsLines[line][character])
                amounts.append(1)
                perimeters.append(0)
            else:
                amounts[charactersIncludingVariety.index(uniqueGroupsLines[line][character])] += 1
            for direction in directions:
                try:
                    if uniqueGroupsLines[line+direction[0]][character+direction[1]] != uniqueGroupsLines[line][character]:
                        perimeters[charactersIncludingVariety.index(uniqueGroupsLines[line][character])]+=1
                except:
                    #found edge but dont care
                    perimeters[charactersIncludingVariety.index(uniqueGroupsLines[line][character])]+=1
    print(charactersIncludingVariety,amounts,perimeters,sep="\n")
    for a in range(len(perimeters)):
        sum1+=(perimeters[a]*amounts[a])
print(sum1,sum2)