a = []

with open("score.md", "r") as f:
	for i in range(10):
		a.append(f.readline().split())
		a[i][1] = int(a[i][1])
		a[i][2] = int(a[i][2])
		a[i][3] = int(a[i][3])

print(a)
