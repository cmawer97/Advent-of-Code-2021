with open("Day 2/input.txt") as f:
    data = f.read().splitlines()

xpos = 0
ypos = 0

for i in data:
    command = i.split()[0]
    param = int(i.split()[1])
    if command == "forward":
        xpos += param
    elif command == "down":
        ypos += param
    elif command == "up":
        ypos -= param
    else:
        print("ERROR")
        break

print(ypos*xpos)