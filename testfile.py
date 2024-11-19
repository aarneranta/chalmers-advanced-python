import json
from pprint import pprint



with open ("labs/data/tramlines.txt", "r", encoding= "UTF-8") as file:
    lines = file.read().replace(":","").strip().split("\n\n")
    lines = [line.split("\n") for line in lines]
print(lines)
test1 = []
test2 =[]
for line in lines:
    stoplist = []
    test2.append(line[0])
    for i in range(1, len(line)):
        item1, item2= [item.strip() for item in line[i].split("  ") if item]
        stoplist.append((item1))
    test1.append(stoplist)
    




print(test1)
print(test2)