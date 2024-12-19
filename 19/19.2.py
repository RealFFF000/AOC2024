from functools import cache
sum1 = 0

@cache
def islegal(string, bit):
    localsum = 0
    if bit == len(string):
        return 1
    for string in strings:
        lenght = len(string)
        if string[bit : bit + lenght] == string:
            localsum += islegal(string, bit + lenght)
    return localsum

with open('input.txt') as input:
    lines = input.readlines()
    bit = []
    bits = []
    strings = []

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
    sum1 = sum(islegal(string,bits) for string in strings)
    print(sum1)