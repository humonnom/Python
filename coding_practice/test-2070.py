num_list = list(map(int, input().split()))
if num_list[0] == num_list[1]:
	result = "="
elif num_list[0] > num_list[1]:
	result = ">"
else:
	result = "<"
