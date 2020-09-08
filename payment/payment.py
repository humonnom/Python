import time
pay = []
i = 0;
j = 0
t = 0
with open("payment.md") as md:
	for line in md.readlines():
		pay.append(line.split())
		if (pay[i][0] == "j"):
			pay[i][0] = "Jueun"
			j += int(pay[i][2])/int(pay[i][3])			
		else:
			pay[i][0] = "Taeseok"
			t += int(pay[i][2])/int(pay[i][3])
		menu_len = len(pay[i][1])
		blank = 10 - menu_len
		half_blank = int(blank / 2)
		pay[i][1] = "|" + ("　" * half_blank) + pay[i][1] + ("　" * int(blank - half_blank)) + "|"
		i += 1

num = 0
title = "Payment"
print("\n{:=^50}\n".format(title))
print(" {:^7}|{:^16}|{:^12}".format("😎", " 🍙🍔🍜🦴 ", " 💸 / 🧍 or 🧍🧍"))
print("------------------------------------------------")
for num in range(i):
	print("{:^9}{}　　{}".format(pay[num][0], pay[num][1], pay[num][2]+"/"+pay[num][3]))
	num += 1
title = "Result⚖️ "
print("\n{:=^50}\n".format(title))
print("	{}".format("Jueun : 총" + str(int(j)) + "원 냈습니다."))
print("	{}".format("Taeseok : 총" + str(int(t)) + "원 냈습니다."))
print("	{}".format("Reseult is ...❇️💰"))
time.sleep(1)
print("	+-------------------------+")
print("	|                         |")
if j == t:
	print("	|          쌤쌤!          |")
	print("	|     Jueun과 Taeseok이   |")
	print("	|   같은 금액을 썼습니다. |")
if j > t:
	print("	|        Jueun Win!       |")
	print("	|   Taeseok이 Jueun에게   |")
	print("	|{:^6}{:^12}|".format(int(j - t), "(원)을 지불하세요"))
if t > j:
	print("	|       Taeseok Win!      |")
	print("	|   Jueun이 Taeseok에게   |")
	print("	|{:^5}{:^13}|".format(int(t - j), "(원)을 지불하세요"))
print("	|                         |")
print("	+-------------------------+")
print("\n{:=^50}\n".format(""))
