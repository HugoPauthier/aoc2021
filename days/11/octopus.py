import numpy as np
from numpy.lib.index_tricks import nd_grid


def prepare_data(filename):
    """Gets the data from the specified file"""
    res = []
    with open(filename) as file:
        data = file.read().splitlines()
        for line in data:
            curr_row = [int(n) for n in line]
            res.append(curr_row)
    return np.array(res)


test_array = prepare_data('test_input.txt')
input_array = prepare_data('input.txt')
# print('INIT\n', test_array, '\n')


def parse_around(energy_array, i, j, flashed):
    flash_count = 0
    # print('parsing', i, j, '\n', energy_array)
    curr_point = energy_array[i, j]
    if curr_point > 9:
        energy_array[i, j] = 0
        # print('FLASH')
        flash_count += 1
        flashed.append([i, j])
        if i >= 0:
            if i > 0:
                # above
                if energy_array[i - 1, j] != 0:
                    energy_array[i - 1, j] += 1
                    flash_count += parse_around(energy_array, i - 1, j, flashed)
                if j > 0:
                    # above - left
                    if energy_array[i - 1, j - 1] != 0:
                        energy_array[i - 1, j - 1] += 1
                        flash_count += parse_around(energy_array, i - 1, j - 1, flashed)
                if j < len(energy_array[0, :]) - 1:
                    # above - right
                    if energy_array[i - 1, j + 1] != 0:
                        energy_array[i - 1, j + 1] += 1
                        flash_count += parse_around(energy_array, i - 1, j + 1, flashed)
            if i < len(energy_array[:, 0]) - 1:
                # below
                if energy_array[i + 1, j] != 0:
                    energy_array[i + 1, j] += 1
                    flash_count += parse_around(energy_array, i + 1, j, flashed)
                if j > 0:
                    # below - left
                    if energy_array[i + 1, j - 1] != 0:
                        energy_array[i + 1, j - 1] += 1
                        flash_count += parse_around(energy_array, i - 1, j - 1, flashed)
                if j < len(energy_array[0, :]) - 1:
                    # below - right
                    if energy_array[i + 1, j + 1] != 0:
                        energy_array[i + 1, j + 1] += 1
                        flash_count += parse_around(energy_array, i - 1, j + 1, flashed)
        if j >= 0:
            if j > 0:
                # left
                if energy_array[i, j - 1] != 0:
                    energy_array[i, j - 1] += 1
                    flash_count += parse_around(energy_array, i, j - 1, flashed)
            if j < len(energy_array[0, :]) - 1:
                # right
                if energy_array[i, j + 1] != 0:
                    energy_array[i, j + 1] += 1
                    flash_count += parse_around(energy_array, i, j + 1, flashed)
    return flash_count

def parse_around2(energy_array, i, j, flashed):
    curr_point = energy_array[i, j]
    if [i, j] not in flashed:
        if curr_point > 9:
            energy_array[i, j] = 0
            flashed.append([i, j])
            if i >= 0:
                if i > 0:
                    # above
                    energy_array[i - 1, j] += 1
                    parse_around2(energy_array, i - 1, j, flashed)
                if i < len(energy_array[:, 0]) - 1:
                    # below
                    energy_array[i + 1, j] += 1
                    parse_around2(energy_array, i + 1, j, flashed)
            if j >= 0:
                if j > 0:
                    # left
                    energy_array[i, j - 1] += 1
                    parse_around2(energy_array, i, j - 1, flashed)
                if j < len(energy_array[0, :]) - 1:
                    # right
                    energy_array[i, j + 1] += 1
                    parse_around2(energy_array, i, j + 1, flashed)
            if (i > 0 and j < len(energy_array[0, :]) - 1):
                # above - right
                energy_array[i - 1, j + 1] += 1
                parse_around2(energy_array, i - 1, j + 1, flashed)
            if (i < len(energy_array[:, 0]) - 1 and j < len(energy_array[0, :]) - 1):
                # below - right
                energy_array[i + 1, j + 1] += 1
                parse_around2(energy_array, i - 1, j + 1, flashed)
            if (i > 0 and j > 0):
                # above - left
                energy_array[i - 1, j - 1] += 1
                parse_around2(energy_array, i - 1, j - 1, flashed)
            if (i < len(energy_array[:, 0]) - 1 and j > 0):
                # below - left
                energy_array[i + 1, j - 1] += 1
                parse_around2(energy_array, i + 1, j - 1, flashed)
    return flashed

test_array30 = np.array([[0,6,4,3,3,3,4,1,1,8],[4,2,5,3,3,3,4,6,1,1],[3,3,7,4,3,3,3,4,5,8],[2,2,2,5,3,3,3,3,3,7],[2,2,2,9,3,3,3,3,3,8],[2,2,7,6,7,3,3,3,3,3],[2,7,5,4,5,7,4,5,6,5],[5,5,4,4,4,5,8,5,1,1],[9,4,4,4,4,4,7,1,1,1],[7,9,4,4,4,4,6,1,1,9]])


def step(energy_array, n):
    flash_count = 0
    flashed = []
    # print('before incr of step ', n, '\n', energy_array)
    # the energy level of each octopus increases by 1
    for i in range(0, len(energy_array[:, 0])):
        for j in range(0, len(energy_array[0, :])):
            energy_array[i, j] += 1
    # print('after incr of step ', n, '\n', energy_array)
    # Then, any octopus with an energy level greater than 9 flashes.
    for i in range(0, len(energy_array[:, 0])):
        for j in range(0, len(energy_array[0, :])):
            # flash_count += parse_around(energy_array, i, j, flashed)
            parse_around2(energy_array, i, j, flashed)

    # print(flashed)
    # print('after step ', n, '\n', energy_array, flash_count)
    return len(flashed)

# print(step(test_array30, 1))

# test_array3 = np.array([[3,0,0,0,0,0,0,8,7,0],[7,10,0,0,0,0,0,0,0,8],[5,7,0,0,0,0,0,0,0,4],[5,6,9,0,0,0,0,0,0,4],[ 5,6,9,0,0,0,0,0,0,5],[ 6,8,2,3,5,0,0,0,0,0],[ 8,1,1,1,2,4,0,0,0,0],[ 1,1,1,1,1,2,3,4,8,6],[ 1,1,1,1,1,1,1,8,6,5],[ 1,1,1,1,1,1,1,6,5,1]])

# step(np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 9]]), 1)
# step(np.array([[1, 1, 1, 1, 1], [1, 9, 9, 9, 1], [1, 9, 9, 9, 1], [1, 9, 9, 9, 1], [1, 1, 1, 1, 1]]), 1)

def part1(energy_array, step_n):
    for n in range(1, step_n + 1):
        step_flashes = step(energy_array, n)
        print(step_flashes)
        # print(energy_array)


print(part1(test_array30, 10))


# print(part1(test_array, 40))
# print(part1(input_array, 100))

def part2(energy_array):
    res = 0
    step_n = 1
    while step_n < 101:
        res = step(energy_array, step_n)
        # print(step_n, 'n flash =', res)
        step_n += 1
    return step_n

# print(part2(test_array))

test_array3 = np.array([[4,1,1,1,1,1,1,9,8,1], [8,11,1,1,1,1,1,1,1,9], [6,8,1,1,1,1,1,1,1,5], [6,7,10,1,1,1,1,1,1,5], [6,7,10,1,1,1,1,1,1,6], [7,9,3,4,6,1,1,1,1,1], [9,2,2,2,3,5,1,1,1,1], [2,2,2,2,2,3,4,5,9,7], [2,2,2,2,2,2,2,9,7,6], [2,2,2,2,2,2,2,7,6,2]])
# print(part1(test_array, 40))