sum1 = 0
sum2 = 0

with open('input.txt') as input:
    #part 1 
    lines = input.readlines()
    string = "XMAS"
    for directionX in range(-1,2):
        for directionY in range(-1,2):
            ranges = [max(0,0-(directionX*3)), max(0,0-(directionY*3)), min(len(lines[0])-1,len(lines[0])-1-(directionX*3)),min(len(lines),len(lines)-(directionY*3))]
            for line in range(ranges[1],ranges[3]):
                for character in range(ranges[0],ranges[2]):
                    legal = True
                    for theString in range(len(string)):
                        if not lines[line+(directionY*theString)][character+(directionX*theString)] == string[theString]:
                            legal = False
                    if legal:
                        sum1 += 1
                
    #part 2
    string = "MAS"
    ranges = [1,1,(len(lines[0])-2),(len(lines)-1)]
    for line in range(ranges[1],ranges[3]):
        for character in range(ranges[0],ranges[2]):
            if lines[line][character] == "A":
                legal = False
                for offset in [-1,1]:
                    if (lines[line+offset][character-offset] == "M" and lines[line-offset][character+offset] == "S"):
                        for otheroffset in [-1,1]:
                            if (lines[line-otheroffset][character-otheroffset] == "M" and lines[line+otheroffset][character+otheroffset] == "S"):
                                legal = True
                if legal:
                    sum2 += 1
print("")
print(sum1,sum2)
