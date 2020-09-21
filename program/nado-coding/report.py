
def title_line(title=''):
	total_len = 20
	if (title):
		total_len = total_len - len(title)
	return ("-" * int(total_len/2) + title + "-" * int(total_len/2))

def write_report():
	n = input('Number:')
	name = input('Name: ')
	summary = input('Summary: ')
	with open(n+'주차.txt', 'w') as file_report:
		file_report.write((title_line("Report") + "\n"))
		file_report.write((n + "주차 주간보고\n"))
		file_report.write(summary + "\n")
		file_report.write(title_line() + "\n")

print("[ Write Report System ]")
write_report()
print(title_line())
