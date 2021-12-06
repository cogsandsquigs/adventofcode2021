l = list(map(lambda x: int(x), open("input.txt", "r").read().split(",")))

def runfishreproduction(fishlist):
    return [b for a in map(lambda x: [x - 1] if x > 0 else [6, 8],fishlist) for b in a]
# print(l)
for _ in range(256):
    l = runfishreproduction(l)
    # print(l)

print(len(l))