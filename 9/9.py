sum1 = 0
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
    cell = 0
    while cell<len(memory):
        try:

            for number in range(len(memory[cell])):
                while memory[cell][number] == ".":
                    memory[cell][number] = memory[-1][-1]
                    memory[-1].pop(-1)
                    while memory[cell] == []:
                        memory.pop(cell)
                    while memory[-1] == []:
                        memory.pop(-1)
        except:
            break
        cell+=1
    #print(memory)
    count = 0
    for a in memory:
        for b in a:
            print(b,end="")
            sum1 += b*count
            count+=1
    
        
                



print("")
print(sum1,sum2)