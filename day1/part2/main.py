t = 0
p1 = 999999999999999
p2 = 999999999999999
p3 = 999999999999999
for i in list(map(lambda x: int(x), open("input.txt", "r").readlines())):
    if p2 + p1 + i > p3 + p2 + p1:
        t += 1
    p3 = p2
    p2 = p1
    p1 = i

print(t)
