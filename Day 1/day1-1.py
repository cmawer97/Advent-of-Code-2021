with open("Day 1/input.txt") as f:
    data = f.read().splitlines()

total = 0

for i in range(0,len(data)-1):
    if int(data[i]) < int(data[i+1]):
        total += 1

print(total)
