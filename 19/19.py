sum1 = 0
shouldBreak = []
with open('input.txt') as input:
    lines = input.readlines()
    bit = []
    bits = []
    strings = []

    def islegal(tempString):
        for bit in range(len(bits)):
            if tempString.startswith(bits[bit]):
                print(tempString,bits[bit],"found")
                if tempString == bits[bit]:
                    legals.append("legal")
                    shouldBreak.append("yes")
                    break
                islegal(tempString[len(bits[bit]):])
                if len(shouldBreak) == 1:
                    break
            else: 
                print(tempString,bits[bit],"not found")

    for line in range(len(lines)):
        if lines[line] == "\n":
            bit = lines[:line]
            strings = lines[line+1:]
    bits = bit[0].split(", ")
    bits[-1] = bits[-1][:-1]
    for string in range(len(strings)):
        if "\n" in strings[string]:
            strings[string] = strings[string][:-1]
    print(bits,strings)
    for string in range(len(strings)):
        shouldBreak = []
        legals = []
        islegal(strings[string])
        if "legal" in legals:
            print("legal")
            sum1+=1
        else:
            print("illegal")
        print("******")
    print(sum1)