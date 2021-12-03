from collections import Counter

with open("Day 3/input.txt") as f:
    data = f.read().splitlines()

oxygenCriteriaList = data.copy()
CO2CriteriaList = data.copy()

while len(oxygenCriteriaList) != 1:
    for i in range(0,len(data[0])):
        counter = Counter([j[i] for j in oxygenCriteriaList])
        if len(oxygenCriteriaList) == 1:
            break
        if counter.get('1') >= counter.get('0'):
            oxygenCriteriaList = [k for k in oxygenCriteriaList if k[i]=='1']
        else:
            oxygenCriteriaList = [k for k in oxygenCriteriaList if k[i]=='0']

while len(CO2CriteriaList) != 1:
    for i in range(0,len(data[0])):
        counter = Counter([j[i] for j in CO2CriteriaList])
        if len(CO2CriteriaList) == 1:
            break
        if counter.get('1') >= counter.get('0'):
            CO2CriteriaList = [k for k in CO2CriteriaList if k[i]=='0']
        else:
            CO2CriteriaList = [k for k in CO2CriteriaList if k[i]=='1']

print(int(oxygenCriteriaList[0], 2) * int(CO2CriteriaList[0], 2))

