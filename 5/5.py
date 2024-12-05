sum1 = 0
sum2 = 0

with open('input.txt') as input:
    # part 1
    lines = input.readlines()
    count = 0
    for line in lines:
        if line == "\n":
            break
        count += 1
    rules = lines[:count]
    checks = lines[count:]
    for rule in range(len(rules)):
        rules[rule] = rules[rule].replace("\n","")
    for check in range(len(checks)):
        checks[check] = checks[check].replace("\n","")
    
    for line in checks:
        line = line.split(",")
        legal = True
        for number in range(len(line)):
            for checkEvery in range((number+1),len(line)):
                if (str(line[checkEvery])+"|"+str(line[number])) in rules:
                    legal = False
                else:
                    line[checkEvery],line[number] = line[number],line[checkEvery] #part 2
        middleIndex = int(((len(line)+1)/2)-1)
        if legal:
            print(line[middleIndex])
            try:
                sum1 += int(line[middleIndex])
            except:
                pass #probably some misused "\n" or something

        #part 2
        else:
            try:
                sum2 += int(line[middleIndex])
            except:
                pass #probably some misused "\n" or something
print(sum1,sum2)