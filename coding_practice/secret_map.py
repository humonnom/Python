def solution(n, arr1, arr2):
    def convert_map(arr):
        map = [[0] * n] * n
        for index in range(len(arr)):
            b_string = str(bin(arr[index])[2:])
            b_string = list(b_string.zfill(n))
            map[index] = b_string

        return map

    def compare_maps():
        string = ""
        answer = list("0" * n)
        for index in range(n):
            string = ""
            for index2 in range(n):
                if map1[index][index2] == "0" and map2[index][index2] == "0":
                    string += " "
                else:


r                    string += "#"
            answer[index] = string
        return answer

    map1 = convert_map(arr1)
    map2 = convert_map(arr2)
    answer = compare_maps()
    return answe


n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]
expacted = ["######", "###  #", "##  ##", " #### ", " #####", "### # "]
result = solution(n, arr1, arr2)
