with open("Day 2/input.txt") as f:
    data = f.read().splitlines()

xpos = 0
ypos = 0
aim = 0

for i in data:
    command = i.split()[0]
    param = int(i.split()[1])
    if command == "forward":
        xpos += param
        ypos += (aim*param)
    elif command == "down":
        aim += param
    elif command == "up":
        aim -= param
    else:
        print("ERROR")
        break

print(ypos*xpos)