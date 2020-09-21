def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = ""
    print("p:{} c:{}".format(participant, completion))
    for index in range(len(completion)):
        print("p[{0}]:{1} c[{0}]:{2}".format(
            index, participant[index], completion[index]))
        if participant[index] != completion[index]:
            return participant[index]
    return participant[-1]


participant = ["marina", "josipa", "nikola", "nikola", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
#participant = completion * 1000 + ["jueun"]
print(solution(participant, completion))
