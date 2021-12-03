c = 0
l = list(map(lambda x: list(x)[:-1], open("input.txt", "r").readlines()))
for j in range(12):
	for x in l:
		c += int(x[j] == '1') * 2 - 1
	if c < 0:
		l = list(filter(lambda x: x[j] == "0", l))
	if c >= 0:
		l = list(filter(lambda x: x[j] == "1", l))
	c = 0
n1 = int(''.join(l[0]), 2)
print(n1)

c = 0
l = list(map(lambda x: list(x)[:-1], open("input.txt", "r").readlines()))
for j in range(12):
	if len(l) == 1:
		break
	for x in l:
		c += int(x[j] == '1') * 2 - 1
	if c >= 0:
		l = list(filter(lambda x: x[j] == "0", l))
	if c < 0:
		l = list(filter(lambda x: x[j] == "1", l))
	print(l)
	c = 0
n2 = int(''.join(l[0]), 2)
print(n1 * n2)