with open("Day 3/input.txt") as f:
    data = f.read().splitlines()

gammaString = ""
epsilonString = ""

for i in range(0,len(data[0])):
    zeros = 0
    ones = 0
    for j in data:
        if j[i] == '0':
            zeros += 1
        else: 
            ones += 1
    if zeros > ones:
        gammaString += '0'
        epsilonString += '1'
    else:
        gammaString += '1'
        epsilonString += '0'

print(int(gammaString, 2) * int(epsilonString, 2))