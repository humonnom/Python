def solution(N, stages):

    def fill_numer(max, stages):
        numer_list = [0] * (max + 1)
        for index in range(len(stages)):
            numer_list[stages[index]] += 1
        return numer_list

    def fill_deno(N, numer_list):
        denomin_list = [0] * (N + 1)
        for index in range(len(denomin_list)):
            if index < 2:
                denomin_list[1] = sum(numer_list)
            else:
                denomin_list[index] = denomin_list[index - 1] - \
                    numer_list[index - 1]

        return denomin_list

    def get_values(size, numer_list, denomin_list):
        values = [0.0] * size
        for index in range(len(values)):
            if denomin_list[index] == 0:
                values[index] = [0, index]
            else:
                values[index] = [numer_list[index]/denomin_list[index], index]
        del values[0]
        values = sorted(values, key=lambda x: (-x[0], x[1]))
        values = list(zip(*values))[1]
        return values

    stages.sort()

    if N < stages[-1]:
        max = N + 1
    else:
        max = N
    # print(stages)
    numer_list = fill_numer(max, stages)
    #print("numer_list :", numer_list)
    denomin_list = fill_deno(N, numer_list)
    #print("denomin_list :", denomin_list)
    values = get_values(N + 1, numer_list, denomin_list)
    print("values:", values)

    # return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
solution(N, stages)

N = 4
stages = [4, 4, 4, 4, 4]
# result = solution(N, stages)
solution(N, stages)
# if result == [3, 4, 2, 1, 5]:
#    print("Corrent")
