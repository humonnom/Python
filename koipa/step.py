while True:

	step = int(input("Input(Exit = 0):" ))
	if step == 0:
		print("Bye")
		break
	
	if step	> 1 and step <= 9:
		print("\nPrint")
		for i in range(0, 10):
			print("{} * {} = {:3d}" .format(step, i, step*i))
	else :
		print("Wrong number")

