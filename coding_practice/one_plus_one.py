def solution(numbers):
    result = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                result.append(numbers[i]+numbers[j])
    result.sort()
    result = list(set(result))
    result.sort()
    return result


numbers = [2, 1, 3, 4, 1]
expacted = [2, 3, 4, 5, 6, 7]
my_reult = solution(numbers)
print(my_reult)
if expacted == my_reult:
    print("OK")
