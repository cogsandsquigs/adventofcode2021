h = 0
v = 0

for i in list(map(lambda x: (x.split(" ")[0], int(x.split(" ")[1])), open("input.txt", "r").readlines())):
	if i[0] == "forward":
		h += i[1]
	elif i[0] == "down":
		v += i[1]
	elif i[0] == "up":
		v -= i[1]

print(h * v)