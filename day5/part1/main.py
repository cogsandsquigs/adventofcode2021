l = list(
    filter(
        lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1],
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
    for m in range(dx + 1):
        for n in range(dy + 1):
            p.append([i[0][0] + m * dxs, i[0][1] + n * dys])
    u.append(p)

s = 0

for i in range(len(u)):
    for j in range(len(u)):
        if i == j:
            pass
        else:
            for m in u[i]:
                for n in u[j]:
                    if m == n:
                        s += 1

print(s)
