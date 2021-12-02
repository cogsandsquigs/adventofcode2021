t = 0
p = 99999
for i in list(map(lambda x: int(x), open("input.txt", "r").readlines())):
    if i > p:
        t += 1
    p = i

print(t)
