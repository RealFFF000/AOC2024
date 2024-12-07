sum1 = 0
sum2 = 0

def base3(num):  
    quotient = num/3    
    remainder = num%3
    if quotient == 0:
        return ""
    else:
        return base3(int(quotient)) + str(int(remainder))
with open('input.txt') as input:
    # part 2
    print("this can take some time")
    lines = input.readlines()
    for line in lines:
        line = str(line)
        localSum = int(line.split(":")[0])
        products = line.split(":")[1][1:].split(" ") 
        for product in range(len(products)):
            products[product] = int(products[product])
        #print(localSum,products)
        legal = False
        for trinaryCounter in range(3**(len(products)-1)):
            trinaryNumber = base3(trinaryCounter)
            temporarySum = 0
            stringSnapshot = []
            for bit in range(len((bin((2**(len(products)-1)))[2:])),0,-1):
                if bit>len(str(trinaryNumber)):
                    temporarySum += (products[len(products)-bit])
                    #print("+",products[len(products)-bit],end=" ")
                    
                else:
                    if (str(trinaryNumber)[-bit] == "0"):
                        temporarySum += (products[len(products)-bit])
                        #print("+",products[len(products)-bit],end=" ")
                    elif (str(trinaryNumber)[-bit] == "1"):
                        temporarySum *= (products[len(products)-bit])
                        #print("*",products[len(products)-bit],end=" ")
                    elif (str(trinaryNumber)[-bit] == "2"):
                        temporarySum = int(str(temporarySum) + str((products[len(products)-bit])))
                        #print("|",products[len(products)-bit],end=" ")
            
            #finalString = str(temporarySum)
            #print(stringSnapshot)
            #for string in reversed(stringSnapshot):
            #    finalString = str(string)+str(finalString)
            #print(temporarySum,localSum)
            #print("\n")
            if localSum == temporarySum:
                legal = True
        if legal:
            print("found one")
            sum1 += localSum
print(sum1,sum2)