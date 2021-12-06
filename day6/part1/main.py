l = list(map(lambda x: int(x), open("input.txt", "r").read().split(",")))

def runfishreproduction(fishlist):
    return [b for a in map(lambda x: [x - 1] if x > 0 else [6, 8],fishlist) for b in a]

for _ in range(80):
    l = runfishreproduction(l)

print(len(l))