import numpy as np

test_input = ['2199943210', '3987894921',
              '9856789892', '8767896789', '9899965678']


def prepare_data(height_list):
    res = []
    for line in height_list:
        split_line = []
        for char in line:
            split_line.append(int(char))
        res.append(split_line)
    return np.array(res)


test_heightmap = prepare_data(test_input)


def is_low_point(heightmap, i, j):
    curr = heightmap[i, j]
    if i == 0:
        if j == 0:
            # up left corner
            right = heightmap[i, j + 1]
            below = heightmap[i + 1, j]
            return ((curr < right) and (curr < below))
        elif j == len(heightmap[0, :]) - 1:
            # up right corner
            left = heightmap[i, j - 1]
            below = heightmap[i + 1, j]
            return ((curr < left) and (curr < below))
        else:
            right = heightmap[i, j + 1]
            left = heightmap[i, j - 1]
            below = heightmap[i + 1, j]
            return ((curr < right) and (curr < left) and (curr < below))
    elif i == len(heightmap[:, 0]) - 1:
        if j == 0:
            # bottom left corner
            right = heightmap[i, j + 1]
            above = heightmap[i - 1, j]
            return ((curr < right) and (curr < above))
        elif j == len(heightmap[0, :]) - 1:
            # bottom right corner
            left = heightmap[i, j - 1]
            above = heightmap[i - 1, j]
            return ((curr < left) and (curr < above))
        else:
            right = heightmap[i, j + 1]
            left = heightmap[i, j - 1]
            above = heightmap[i - 1, j]
            return ((curr < right) and (curr < left) and (curr < above))
    else:
        if j == 0:
            right = heightmap[i, j + 1]
            above = heightmap[i - 1, j]
            below = heightmap[i + 1, j]
            return ((curr < right) and (curr < above) and (curr < below))
        elif j == len(heightmap[0, :]) - 1:
            left = heightmap[i, j - 1]
            above = heightmap[i - 1, j]
            below = heightmap[i + 1, j]
            return ((curr < left) and (curr < above) and (curr < below))
        else:
            right = heightmap[i, j + 1]
            left = heightmap[i, j - 1]
            above = heightmap[i - 1, j]
            below = heightmap[i + 1, j]
            return ((curr < right) and (curr < left) and (curr < above) and (curr < below))


assert is_low_point(test_heightmap, 0, 1) == True
assert is_low_point(test_heightmap, 0, 9) == True
assert is_low_point(test_heightmap, 0, 0) == False
assert is_low_point(test_heightmap, 4, 6) == True
assert is_low_point(test_heightmap, 4, 0) == False
assert is_low_point(test_heightmap, 2, 2) == True
assert is_low_point(test_heightmap, 1, 1) == False
assert is_low_point(test_heightmap, 1, 9) == False


def get_risk_level_sum(heightmap, low_points):
    res = 0
    for point in low_points:
        curr_point = heightmap[point[0], point[1]]
        res += curr_point + 1
    return res


assert get_risk_level_sum(
    test_heightmap, [[0, 1], [0, 9], [2, 2], [4, 6]]) == 15


def find_low_points(heightmap):
    res = []
    for i in range(len(heightmap[:, 0])):
        for j in range(len(heightmap[0, :])):
            if is_low_point(heightmap, i, j):
                res.append([i, j])
    return res


def part1(heightmap):
    low_points = find_low_points(heightmap)
    # print(low_points)
    risk_level_sum = get_risk_level_sum(heightmap, low_points)
    # print(risk_level_sum)
    return risk_level_sum
