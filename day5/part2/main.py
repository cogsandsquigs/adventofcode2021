l = list(
    filter(
        lambda x: x,
        map(
            lambda x: list(
                [
                    list(map(lambda x: int(x), x.replace(" -> ", ",").split(",")[0:2])),
                    list(map(lambda x: int(x), x.replace(" -> ", ",").split(",")[2:4])),
                ],
            ),
            open("input.txt", "r").readlines(),
        ),
    )
)

sign = lambda a: (a > 0) - (a < 0)

u = []
for i in l:
    dx = abs(i[1][0] - i[0][0])
    dxs = sign(i[1][0] - i[0][0])
    dy = abs(i[1][1] - i[0][1])
    dys = sign(i[1][1] - i[0][1])
    p = []
    if dx == dy:
        for m, n in zip(range(dx+1), range(dy+1)):
            p.append([i[0][0] + m * dxs, i[0][1] + n * dys])
    else:
        for m in range(dx + 1):
            for n in range(dy + 1):
                p.append([i[0][0] + m * dxs, i[0][1] + n * dys])
    u.append(p)
u = [a for b in u for a in b]
s = 0
sb = [ [0] * 999 for _ in range(999)]

for c in u:
	sb[c[1]][c[0]] += 1

for q in [a for b in sb for a in b]:
	if q > 1:
		s += 1

print(s)
