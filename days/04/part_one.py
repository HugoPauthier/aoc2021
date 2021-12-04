import numpy as np

with open('input.txt') as file:
    test_input = file.read().splitlines()

    order_numbers = [int(n) for n in test_input[0].split(',')]
    boards_matrix = []
    board = []
    for i in range(2, len(test_input)):
        current = test_input[i]
        if current == '':
            # Its a board delimiter
            matrix = np.array(board)
            boards_matrix.append(matrix)
            board = []
        else:
            # Tis a new board row
            curr_row = [int(n) for n in current.split()]
            board.append(curr_row)
    boards_matrix.append(np.array(board))


test_repl = np.array([[1, 4], [3, 4]])
test_r = np.array([[1, 2], [np.nan, np.nan]])
test_c = np.array([[1, np.nan], [2, np.nan]])


def replace_val(val, bboard):
    return np.where(bboard == val, np.nan, bboard)


def check_row(index, bboard):
    return all([np.isnan(x) for x in bboard[index, :]])
    # return all(True for x in bboard[index, :] if np.isnan(x))


assert check_row(0, test_r) == False
assert check_row(1, test_r) == True


def check_col(index, bboard):
    return all([np.isnan(x) for x in bboard[:, index]])
    # return all(True for x in bboard[:, index] if np.isnan(x))


assert check_col(0, test_c) == False
assert check_col(1, test_c) == True


def check_board(bboard):
    for ind in range(len(bboard[0])):
        if check_row(ind, bboard):
            return True
        if check_col(ind, bboard):
            return True
    return False
# print(check_board(test_r))


def part1(order, boards):
    for number in order:
        for k in range(len(boards)):
            boards[k] = replace_val(number, boards[k])
        for b in boards:
            if check_board(b):
                return np.nansum(b * number, dtype=int)
    return False


assert part1(order_numbers, boards_matrix) == 63424
