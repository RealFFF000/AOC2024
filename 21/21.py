sum1 = 0
keypad1 = [
    ["7","8","9"],
    ["4","5","6"],
    ["1","2","3"],
    ["#","0","A"]
]
keypad2 = [
    ["#","^","A"],
    ["<","v",">"]
]
#keypad1
#789
#456
#123
# 0A

#keypad2
# ^A
#<v>

def keypad1_coords(character):
    match character:
        case "A":
            return [2,3]
        case "0":
            return [1,3]
        case "1":
            return [0,2]
        case "2":
            return [1,2]
        case "3":
            return [2,2]
        case "4":
            return [0,1]
        case "5":
            return [1,1]
        case "6":
            return [2,1]
        case "7":
            return [0,0]
        case "8":
            return [1,0]
        case "9":
            return [2,0]
def keypad2_coords(character):
    match character:
        case "^":
            return [1,0]
        case "A":
            return [2,0]
        case "<":
            return [0,1]
        case "v":
            return [1,1]
        case ">":
            return [2,1]
# we control a keypad2 instance to give orders to another keypad2 which will give orders to keypad1 (keypad1 needs to input our number)
def keypad1_to_keypad2(character1,character2):
    toRetrurn = ""
    delta = [keypad1_coords(character1)[0]-keypad1_coords(character2)[0],keypad1_coords(character1)[1]-keypad1_coords(character2)[1]]
    if delta[0] > 0:
        for a in range(delta[0]):
            toRetrurn += "<"
    elif delta[0] <0:
        for a in range(abs(delta[0])):
            toRetrurn += ">"
    if delta[1] > 0:
        for a in range(delta[1]):
            toRetrurn += "^"
    elif delta[1] < 0:
        for a in range(abs(delta[1])):
            toRetrurn += "v"
    

    return (toRetrurn+"A")
def keypad2_to_keypad2(character1,character2):
    toRetrurn = ""
    delta = [keypad2_coords(character1)[0]-keypad2_coords(character2)[0],keypad2_coords(character1)[1]-keypad2_coords(character2)[1]]
    if delta[1] > 0:
        for a in range(delta[1]):
            toRetrurn += "^"
    elif delta[1] < 0:
        for a in range(abs(delta[1])):
            toRetrurn += "v"
    
    if delta[0] > 0:
        for a in range(delta[0]):
            toRetrurn += "<"
    elif delta[0] <0:
        for a in range(abs(delta[0])):
            toRetrurn += ">"
    return (toRetrurn+"A")  

with open('input.txt') as input:
    lines = input.readlines()
    for line in lines:
        line = line.replace("\n","")
        characters = keypad1_to_keypad2("A",line[0])
        for character in range(len(line)-1):
            characters += keypad1_to_keypad2(line[character],line[character+1])
        characters2 = keypad2_to_keypad2("A",characters[0])
        for character in range(len(characters)-1):
            characters2+=keypad2_to_keypad2(characters[character],characters[character+1])
        
        finalString = keypad2_to_keypad2("A",characters2[0])
        for character in range(len(characters2)-1):
            finalString+= keypad2_to_keypad2(characters2[character],characters2[character+1])
        #print(line)
        #print(characters)
        #print(characters2)
        #print(finalString)
        number = ''.join(filter(lambda i: i.isdigit(), line))
        print(len(finalString),int(number),len(finalString)*int(number))
        sum1+=len(finalString)*int(number)
print(sum1)
