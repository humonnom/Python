

def solution(map, moves):
    def grep_a_doll():
        if sum(target_line) == 0:
            return(0, 0)
        target = [i for i in target_line if i != 0]
        print("*target:", target[0])
        print("*row:", target_line.index(target[0]))
        print("*target_line: ", target_line)
        return(target_line.index(target[0]), target[0])

    def fill_basket():
        basket.append(target)
        print("filed : ", basket)
        return(basket)

    def pop_basket():
        count = 0
        if (len(basket)) >= 2:
            if basket[-1] == basket[-2]:
                del basket[-1]
                del basket[-1]
                count += 2
        return(basket, count)

    def print_map(map, basket):
        for i in range(5):
            print(map[i])
        print("\n", basket)

    total = 0
    target = [0]
    map_len = len(map) * len(map[0])
    basket = []

    for index in range(len(moves)):
        print("=====index:{} target_line:{}=====".format(index, moves[index]))
        target_line = list(zip(* map))[moves[index] - 1]
        row, target = grep_a_doll()
        print_map(map, basket)
        print("⇩")
        print("tager :", target)
        if target != 0:
            basket = fill_basket()
            basket, count = pop_basket()
            total += count
            print("row: {}, col: {}".format(row, (moves[index]) - 1))
            map[row][moves[index] - 1] = 0
        print_map(map, basket)

    return total


board = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]]

moves = [1, 5, 3, 5, 1, 2, 1, 4]

result = solution(board, moves)
# print(result)
