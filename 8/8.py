sum1 = 0
sum2 = 0

with open('input.txt') as input:
    # part 1
    lines = input.readlines()
    antinodes = []
    for line in range(len(lines)):
        lines[line].replace("\n","")
        for character in range(len(lines[line])):
            if lines[line][character] != ".":
                foundletter = str(lines[line][character])
                for innerLine in range(len(lines)):
                    lines[innerLine].replace("\n","")
                    for innerCharacter in range(len(lines[innerLine])):
                        if lines[innerLine][innerCharacter] == foundletter and [innerLine,innerCharacter] != [line,character]:
                            offset = [innerLine-line,innerCharacter-character]
                            antinode = [innerLine,innerCharacter]
                            count = 0
                            while True:
                                if antinode[0] in range(len(lines)) and antinode[1] in range(len(lines[line])-1):
                                    if [antinode[0],antinode[1]] not in antinodes:
                                        antinodes.append([antinode[0],antinode[1]])
                                        if count == 1:
                                            sum1 += 1
                                else:
                                    break
                                antinode[0] += offset[0]
                                antinode[1] += offset[1]
                                count += 1

    sum2 = len(antinodes)
    
    
    for line in range(len(lines)):
        for character in range(len(lines[line])):
            if lines[line][character] == ".":
                if [line,character] in antinodes:
                    print("#",end="")
                else:
                    print(lines[line][character],end="")
            else:
                    print(lines[line][character],end="")
        
    
    print(antinodes)
print(sum1,sum2)