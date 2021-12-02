h = 0
v = 0
a = 0
for t, x in list(map(lambda x: (x.split(" ")[0], int(x.split(" ")[1])), open("input.txt", "r").readlines())):
	if t == "forward":
		h += x
		v += a * x
	elif t == "down":
		a += x
	elif t == "up":
		a -= x
	print(t, x, ": ", h, v, a)

print(h * v)