import re


def solution(dartResult):
    n = 3

    bundle = [0] * n
    score = [0] * n
    bonus = [0] * n
    option = ["none"] * n

    score = re.findall("\d+", dartResult)
    index1 = dartResult.index(score[0])
    index2 = dartResult.index(score[1])
    index3 = dartResult.index(score[2])

    bundle[0] = dartResult[index1:index2]
    bundle[1] = dartResult[index2:index3]
    bundle[2] = dartResult[index3:]

    for index in range(n):
        score[index] = int(score[index])
        if score[index] == 10:
            bundle[index] = bundle[index][2:]
        else:
            bundle[index] = bundle[index][1:]
        if len(bundle[index]) == 2:
            option[index] = bundle[index][-1]
        bonus[index] = bundle[index][0]

    for index in range(n):
        if bonus[index] == 'S':
            squared = 1
        elif bonus[index] == 'D':
            squared = 2
        else:
            squared = 3
        score[index] = score[index] ** squared

    for index in range(n):
        if option[index] == "*" and index > 0:
            if option[index - 1] == "none":
                option[index - 1] = "*"
            else:
                option[index - 1] += "*"

    for index in range(n):
        effect = 1
        option_len = len(option[index])
        if option_len == 2:
            if option[index] == "**":
                effect = 4
            elif option[index] == "##":
                effect = -4
            elif option[index] == "*#" or option[index] == "#*":
                effect *= -2
        if option_len == 1:
            if option[index] == "*":
                effect = 2
            elif option[index] == "#":
                effect = -1
        score[index] *= effect

    answer = sum(score)
    return answer


dartResult = "1D2S3T*"
print(solution(dartResult))
