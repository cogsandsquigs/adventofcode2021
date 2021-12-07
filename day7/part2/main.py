import math
crabs = sorted(list(map(lambda x: int(x), open("input.txt", "r").readlines()[0].split(","))))
medl = crabs[math.ceil(len(crabs)/2)]
psumfuel = 9999999999999999
sumfuel = 0
for l in range(crabs[0], crabs[-1] + 1):
    for i in crabs:
        sumfuel += (abs(i-l) * (abs(i - l) + 1)) / 2
    if psumfuel > sumfuel:
        psumfuel = sumfuel
    sumfuel = 0

print(psumfuel)