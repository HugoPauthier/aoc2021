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


def parse_around(heightmap, i, j, points):
    if [i, j] in points:
        return 0
    points.append([i, j])
    count = 1
    curr_point = heightmap[i, j]
    if i >= 0:
        if i > 0:
            above = heightmap[i - 1, j]
            # if above == curr_point + 1 and above != 9:
            if above > curr_point and above != 9:
                count += parse_around(heightmap, i - 1, j, points)
        if i < len(heightmap[:, 0]) - 1:
            below = heightmap[i + 1, j]
            # if below == curr_point + 1 and below != 9:
            if below > curr_point and below != 9:
                count += parse_around(heightmap, i + 1, j, points)
    if j >= 0:
        if j > 0:
            left = heightmap[i, j - 1]
            # if left == curr_point + 1 and left != 9:
            if left > curr_point and left != 9:
                count += parse_around(heightmap, i, j - 1, points)
        if j < len(heightmap[0, :]) - 1:
            right = heightmap[i, j + 1]
            # if right == curr_point + 1 and right != 9:
            if right > curr_point and right != 9:
                count += parse_around(heightmap, i, j + 1, points)
    return count


def part2(heightmap):
    low_points = find_low_points(heightmap)
    res = []
    points = []
    for low_point in low_points:
        basins_lentgh = parse_around(heightmap, low_point[0], low_point[1], points)
        res.append(basins_lentgh)
    # print(parse_around(test_heightmap, 0, 1, []))
    res.sort(reverse=True)
    # print(res, len(res))
    return (res[0] * res[1] * res[2])

assert part2(test_heightmap) == 1134