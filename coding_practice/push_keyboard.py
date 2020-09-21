def get_diff(num1, num2):
    if num1 > num2:
        return num1-num2
    else:
        return num2-num1


def solution(numbers, hand):
    answer = ''
    map = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ["*", 0, "#"]
    ]
    left_zone = [1, 4, 7]
    right_zone = [3, 6, 9]
    middle_zone = [2, 5, 8, 0]
    r_current = [3, 2]
    l_current = [3, 0]

    for index in range(len(numbers)):
        target = numbers[index]
        if target > 0:
            row = int((target - 1)/3)
            col = map[row].index(target)
        else:
            row = 3
            col = 1
        if target in left_zone:
            answer += "L"
            l_current = [row, col]
        elif target in right_zone:
            answer += "R"
            r_current = [row, col]
        else:
            r_diff = get_diff(row, r_current[0]) + get_diff(col, r_current[1])
            l_diff = get_diff(row, l_current[0]) + get_diff(col, l_current[1])
            if l_diff < r_diff:
                answer += "L"
                l_current = [row, col]
            elif r_diff < l_diff:
                answer += "R"
                r_current = [row, col]
            else:
                if hand == "right":
                    answer += "R"
                    r_current = [row, col]
                else:
                    answer += "L"
                    l_current = [row, col]
    return answer


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"
print(solution(numbers, hand))
