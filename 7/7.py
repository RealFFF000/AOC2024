sum1 = 0
sum2 = 0

with open('input.txt') as input:
    # part 1
    lines = input.readlines()
    for line in lines:
        line = str(line)
        localSum = int(line.split(":")[0])
        products = line.split(":")[1][1:].split(" ") 
        for product in range(len(products)):
            products[product] = int(products[product])
        #print(localSum,products)
        legal = False
        for binaryCounter in range(2**(len(products)-1)):
            binaryNumber = bin(binaryCounter)[2:]
            temporarySum = 0
            for bit in range(len((bin((2**(len(products)-1)))[2:])),0,-1):
                if bit>len(str(binaryNumber)):
                    temporarySum += (products[len(products)-bit])
                    #print("+",products[len(products)-bit],end=" ")
                    
                else:
                    if (str(binaryNumber)[-bit] == "0"):
                        temporarySum += (products[len(products)-bit])
                        #print("+",products[len(products)-bit],end=" ")
                    elif (str(binaryNumber)[-bit] == "1"):
                        temporarySum *= (products[len(products)-bit])
                        #print("*",products[len(products)-bit],end=" ")
            #print("\n")
            if localSum == temporarySum:
                legal = True
        if legal:
            sum1 += localSum
print(sum1,sum2)