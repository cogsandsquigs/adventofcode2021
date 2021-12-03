bl = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for l in list(map(lambda x: list(x)[:-1], open("input.txt", "r").readlines())):
    for i in range(len(l)):
        bl[i] += int(l[i] == '1') * 2 - 1
for i in range(len(bl)):
	if bl[i] < 0:
		bl[i] = "0"
	elif bl[i] > 0:
		bl[i] = "1"
n1 = int("0b" + ''.join(bl), 2)
n2 = n1 ^ 0b111111111111
print(n1 * n2)
