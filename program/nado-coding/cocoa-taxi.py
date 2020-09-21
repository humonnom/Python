from random import *

def cocoa():
	i = 0
	count = 0

	while i < 50:
		flag = ' '
		time = randint(5, 50)
		if time >= 5 and time <= 15:
			count += 1
			flag = 'O'
		i += 1
		print("{} {}번째 손님: {}".format("[" + flag + "]", i, time))

	return count

result = cocoa()
print("총 탑승 승객 : ", result, "분")
