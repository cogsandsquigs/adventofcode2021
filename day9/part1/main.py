l = list(map(lambda x: x[:-1], open("input.txt", "r").readlines()))
rows = []
for row in l:
    x = []
    for num in row:
        x.append(int(num))
    rows.append(x)

preliminarylowestindexes = []
for row in rows:
    lowest = 10
    rpli = []
    for num in row:
        if num < lowest:
            lowest = num
    for i in range(len(row)):
        if row[i] == lowest:
            rpli.append(i)
    preliminarylowestindexes.append(rpli)

for a, b, c in zip(row[0:1], row[1:2], row[2:3]):
    for num in row[]:
        
            

print(preliminarylowestindexes)