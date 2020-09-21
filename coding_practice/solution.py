def solution(participant, completion):
    answer = ""
    for index in range(len(participant)):
        print("== == ==" + str(index) + "== == ==")
        flag = False
        print("----"+participant[index]+"----")
        for index2 in range(len(completion)):
            print(index2)
            print("p:{} c:{}".format(participant[index], completion[index2]))
            print(completion)
            if (participant[index] == completion[index2]):
                print("found " + completion[index2])
                del completion[index2]
                flag = True
                break
            print(len(completion)-1)
        if flag == False:
            answer = participant[index]
            break
    return answer


#participant = ["marina", "josipa", "nikola", "nikola", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
participant = completion * 1000 + ["jueun"]
print(solution(participant, completion))
