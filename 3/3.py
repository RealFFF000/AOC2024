sum1 = 0
sum2 = 0
with open('input.txt') as input:
    #part 1
    lines = input.readlines()
    previousProduct = 0
    for line in lines:
        for characters in line:
            if line.startswith("mul("):
                line = line[4:]
                stringOfFactors = line.split(")")[0]
                if "mul(" in stringOfFactors:
                    print(stringOfFactors)
                    while stringOfFactors.startswith("mul(") == False:
                        stringOfFactors = stringOfFactors[1:]
                    stringOfFactors = stringOfFactors[4:]  
                factors = stringOfFactors.split(",")
                try:
                    factors[0] = int(factors[0])
                    factors[1] = int(factors[1])
                    product = factors[0]*factors[1]
                    if previousProduct != product:
                        sum1 += product
                        previousProduct = product
                    print(factors[0],factors[1],product)
                except:
                    product = "some error"
                    #print(factors)
                
                line = line[(len(stringOfFactors)):]
            else:
                line = line[1:]

print(sum1,sum2)