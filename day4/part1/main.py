lastcallednum = -1
numslist = list(map(lambda x: int(x), open("input.txt", "r").readlines()[0].split(",")))
x = list(
    filter(
        lambda x: x != "",
        map(lambda x: x.replace("\n", ""), open("input.txt", "r").readlines()[1:]),
    )
)
boardslist = list(
    map(
        lambda x: x.replace("  ", " "),
        [
            x[i] + " " + x[i + 1] + " " + x[i + 2] + " " + x[i + 3] + " " + x[i + 4]
            if not len(x) % 5
            else None
            for i in range(0, len(x), 5)
        ],
    )
)

print(boardslist)
