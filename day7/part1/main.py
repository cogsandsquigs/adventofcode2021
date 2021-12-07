import math
crabs = sorted(list(map(lambda x: int(x), open("input.txt", "r").readlines()[0].split(","))))
medl = crabs[math.ceil(len(crabs)/2)]
sumfuel = 0
for i in crabs:
    sumfuel += abs(i - medl)

print(sumfuel)