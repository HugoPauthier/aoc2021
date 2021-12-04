import numpy as np


def prepare_data(filename):
    """Gets the data from the specified file"""
    with open(filename) as file:
        data = file.read().splitlines()

        order_numbers = [int(n) for n in data[0].split(',')]
        boards_matrix = []
        board = []
        for i in range(2, len(data)):
            current = data[i]
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
    return order_numbers, boards_matrix


# Some testing value
test_repl = np.array([[1, 4], [3, 4]])
test_r = np.array([[1, 2], [np.nan, np.nan]])
test_c = np.array([[1, np.nan], [2, np.nan]])


def replace_val(val, bboard):
    """It replaces all the val contained in the board by NaN"""
    return np.where(bboard == val, np.nan, bboard)


def check_row(index, bboard):
    """Checks if the specified row is filled with NaN"""
    return all([np.isnan(x) for x in bboard[index, :]])
    # return all(True for x in bboard[index, :] if np.isnan(x))


assert check_row(0, test_r) == False
assert check_row(1, test_r) == True


def check_col(index, bboard):
    """Checks if the specified column is filled with NaN"""
    return all([np.isnan(x) for x in bboard[:, index]])
    # return all(True for x in bboard[:, index] if np.isnan(x))


assert check_col(0, test_c) == False
assert check_col(1, test_c) == True


def check_board(bboard):
    """Checks if the board has a row/column filled with NaN"""
    for ind in range(len(bboard[0])):
        if check_row(ind, bboard):
            return True
        if check_col(ind, bboard):
            return True
    return False
# print(check_board(test_r))


def part1(order, boards):
    """Part one"""
    for number in order:
        for k in range(len(boards)):
            boards[k] = replace_val(number, boards[k])
        for b in boards:
            if check_board(b):
                return np.nansum(b * number, dtype=int)
    return False


(order_numbers, boards_matrix) = prepare_data('test_input.txt')
assert part1(order_numbers, boards_matrix) == 4512


def part2(order, boards):
    """Part two"""
    res = []
    for number in order:
        for k in range(len(boards)):
            boards[k] = replace_val(number, boards[k])
        for i in range(len(boards)):
            if check_board(boards[i]):
                if not (i in res):
                    res.append(i)
        if len(res) == len(boards):
            return (np.nansum(boards[res[-1]] * number, dtype=int))
    return res


(order_numbers, boards_matrix) = prepare_data('test_input.txt')
assert part2(order_numbers, boards_matrix) == 1924
