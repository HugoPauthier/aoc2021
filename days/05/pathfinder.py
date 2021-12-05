import numpy as np


def prepare_data(filename):
    """Gets the data from the specified file"""
    with open(filename) as file:
        data = file.read().splitlines()
        vents_lines = []
        max_x = 0
        max_y = 0
        for line in data:
            split_line = line.split(' -> ')
            start = list(map(int, split_line[0].split(',')))
            if start[0] > max_x:
                max_x = start[0]
            if start[1] > max_y:
                max_y = start[1]
            end = list(map(int, split_line[1].split(',')))
            if end[0] > max_x:
                max_x = end[0]
            if end[1] > max_y:
                max_y = end[1]
            vents_lines.append((start, end))
        return vents_lines, max_x, max_y


def init_diagram(max_x, max_y):
    """Inits a matrix filled with zeros"""
    # print(max_x, max_y)
    diagram = np.zeros((max_y + 1, max_x + 1))
    return diagram


def update_diagram_lines(diagram, start, end):
    """Increments by 1 the point between start - end vertically or horizontally"""
    (x1, y1) = start
    (x2, y2) = end
    for i in range(min([x1, x2]), max([x1, x2]) + 1):
        for j in range(min([y1, y2]), max([y1, y2]) + 1):
            diagram[j, i] += 1
    return diagram


test_diagram = init_diagram(9, 9)

# print(update_diagram_lines(test_diagram, [0, 9], [5, 9]))
# print(update_diagram_lines(test_diagram, [0, 9], [2, 9]))
# print(update_diagram_lines(test_diagram2, [727,990], [727,273]))
assert np.all(update_diagram_lines(test_diagram.copy(), [0, 9], [5, 9])[9, :6])
assert np.all(update_diagram_lines(test_diagram.copy(), [7, 0], [7, 4])[:5, 7])


def update_diagram_diag(diagram, start, end):
    """Increments by 1 the point between start - end diagonally"""
    (x1, y1) = start
    (x2, y2) = end
    # print(start, end)
    if x1 < x2:
        if y1 < y2:
            # x incremente
            # y incremente
            x_range = range(x1, x2 + 1)
            y_range = range(y1, y2 + 1)
            for i in range(len(x_range)):
                diagram[y_range[i], x_range[i]] += 1
        elif y1 > y2:
            # x incremente
            # y decremente
            x_range = range(x1, x2 + 1)
            y_range = range(y1, y2 - 1, - 1)
            for i in range(len(x_range)):
                diagram[y_range[i], x_range[i]] += 1
    elif x1 > x2:

        if y1 < y2:
            # x decremente
            # y incremente
            x_range = range(x1, x2 - 1, -1)
            y_range = range(y1, y2 + 1)
            for i in range(len(x_range)):
                diagram[y_range[i], x_range[i]] += 1

        elif y1 > y2:
            # x decremente
            # y decremente
            x_range = range(x1, x2 - 1, -1)
            y_range = range(y1, y2 - 1, -1)
            for i in range(len(x_range)):
                diagram[y_range[i], x_range[i]] += 1

    return diagram

# print(update_diagram_diag(test_diagram, [0, 0], [3, 3]))
# print(update_diagram_diag(test_diagram.copy(), [8, 0], [0, 8]))
# print(update_diagram_diag(test_diagram.copy(), [0, 8], [8, 0]))
# print(update_diagram_diag(test_diagram.copy(), [6, 4], [2, 0]))
