import numpy as np


def prepare_data(filename):
    """Gets the data from the specified file"""
    with open(filename) as file:
        data = file.read().splitlines()
        return data


def get_dots(data):
    dots = []
    max_x = 0
    max_y = 0
    for i in range(0, len(data)):
        current = data[i]
        if current == "":
            return dots, max_x, max_y, i
        dot_split = [int(x) for x in current.split(",")]
        if dot_split[0] > max_x:
            max_x = dot_split[0]
        if dot_split[1] > max_y:
            max_y = dot_split[1]
        dots.append(dot_split)


def get_folds(data, start):
    folds = []
    for i in range(start + 1, len(data)):
        current = data[i]
        fold_split = current.split("=")
        folds.append([fold_split[0][-1], int(fold_split[1])])
    return folds


def init_paper(max_x, max_y):
    """Inits a matrix filled with zeros"""
    # print(max_x, max_y)
    paper = np.full((max_y + 1, max_x + 1), ".")
    return paper


# test_data = prepare_data("test_input.txt")
# print(test_data)
# get_dots, max_x, max_y, start = get_dots(test_data)
# print(get_dots)
# get_folds = get_folds(test_data, start)
# print(get_folds)
# print(max_x, max_y)
# test_paper = init_paper(max_x, max_y)


def update_paper(paper, dots):
    for [x, y] in dots:
        paper[y, x] = "#"
    return paper


# test_update = update_paper(test_paper, get_dots)
# print(test_update)
# print('\n')


def fold_on_axe(paper, axe, n):
    res = 0
    if axe == "y":
        res = paper[:n, :]
        # print(res)
        for i in range(n + 1, len(paper[:, 0])):
            for j in range(0, len(paper[0, :])):
                if paper[i, j] == "#":
                    # print(i, j, paper[i, j])
                    res[abs(i - 2 * n), j] = "#"
    if axe == "x":
        res = paper[:, :n]
        for i in range(len(paper[:, 0])):
            for j in range(n + 1, len(paper[0, :])):
                if paper[i, j] == "#":
                    # print(i, j, paper[i, j])
                    res[i, abs(j - 2 * n)] = "#"
    return res


def fold_paper(paper, folds):
    res = paper.copy()
    for i in range(0, len(folds)):
        axe = folds[i][0]
        n = folds[i][1]
        # print(axe, n)
        res = fold_on_axe(res, axe, n)
    return res


# fold_x = fold_on_axe(test_update, 'x', 5)
# print(fold_x)
# fold_y = fold_on_axe(fold_x, 'x', 5)
# print(fold_y)


# print(fold_paper(test_paper, get_folds))
