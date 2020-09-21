#import sys
#print("python", "java", file=sys.stdout)
#print("python", "java", file=sys.stderr)

#def example(x = 29, y = 90):
#	print("x - y = ", x - y)
#
#example(100)
#example(31, 21)
#example()
#
##Exam score
#scores = {"math" : 0, "eng":50, "coding" : 90}
#for subject, score in scores.items():
#	print(subject.ljust(8), str(score).rjust(4))
#
##은행 대기번호
#for num in range(1, 21):
#	print("대기번호 :" + str(num).zfill(3))

#answer = input(":")
#print("Input value was "+answer)

#score_file = open("score.txt", "w", encoding="utf8")
#print("math : 50", file=score_file)
#print("eng : 80", file=score_file)
#print("coding : 90", file=score_file)
#score_file.close()

#score_file = open("score.txt", "a", encoding="utf8")
#score_file.write("science : 80")
#score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()
