alpha_string = list(input())
for index in range(len(alpha_string)):
	print(ord(alpha_string[index].lower()) - 96, end = " ")
