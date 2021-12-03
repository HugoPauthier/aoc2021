testReport = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def part1(report):
    """Part one"""
    res = 0
    for i in range(1, len(report)):
        if (report[i] > report[i-1]):
            res += 1
    return res


# Unit test
assert part1(testReport) == 7
