sum1 = 0
sum2 = 0
def isLegal(series):
    print(series)
    sign = 0
    if series[0]>series[1]:
        #print("the series is decreasing")
        sign = -1
    elif series[0]<series[1]:
        #print("the series is increasing")
        sign = 1
    else:
        pass
        #print("the series seems non-changing")

    legal = True
    for number in range(len(series)-1):
        difference = series[number]-series[number+1]
        if sign == 1:
            if difference >= -3 and difference < 0:
                pass
            else:
                legal = False
        else:
            if difference <= 3 and difference > 0:
                pass
            else:
                legal = False
    if legal:
        return(True)

with open('input.txt') as input:
    #part 1 
    lines = input.readlines()
    for line in lines:
        numbers = list(map(int, line.split(" ")))
        if isLegal(numbers):
            sum1+=1
        #part 2
        else:
            for excludedNumber in range(len(numbers)):
                excludedNumbers = numbers.copy()
                excludedNumbers.pop(excludedNumber)
                if isLegal(excludedNumbers):
                    sum2+=1
                    break

sum2 += sum1
print(sum1,sum2)
