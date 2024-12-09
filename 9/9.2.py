sum2 = 0

with open('input.txt') as input:
    # part 1
    lines = input.readlines()
    line = lines[0]
    count = 0
    memory = []
    for character in range(len(line)):
        memory.append([])
        if count%2 == 0:
            for times in range(int(line[character])):
                memory[count].append(int(count/2))
        else:
            for times in range(int(line[character])):
                memory[count].append(".")
        count += 1
    for cell in range(len(memory)):
        try:
            if memory[cell] == []:
                memory.pop(cell)
        except:
            break
    cellFromBeginning = 0
    while cellFromBeginning < len(memory):
        for cellFromEnd in range((len(memory)-1),cellFromBeginning,-1):
            if memory[cellFromBeginning][0] == "." and memory[cellFromEnd][0] != ".":
                if len(memory[cellFromBeginning]) >= len(memory[cellFromEnd]):
                    diff = len(memory[cellFromBeginning]) - len(memory[cellFromEnd])
                    memory[cellFromBeginning] = memory[cellFromEnd]
                    toinsert = []
                    for times in range(len(memory[cellFromEnd])):
                        toinsert.append(".")
                    memory[cellFromEnd] = toinsert
                    


                    if diff != 0:
                        toinsert = []
                        for times in range(diff):
                            toinsert.append(".")
                        memory.insert(cellFromBeginning+1,toinsert)
                    
            
        print(cellFromBeginning)
        cellFromBeginning += 1  
    count = 0
    for a in memory:
        for b in a:
            print(b,end="")
            try:
                sum2 += b*count
            except:
                pass
            count+=1

print("")
print(sum2)