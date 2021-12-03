testReport = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def part2(report):
    """Part two"""
    windows_sum_list = []
    res = 0

    for i in range(1, len(report)-1):
        window_sum = sum(report[i-1:i+2])
        windows_sum_list.append(window_sum)

    for i in range(1, len(windows_sum_list)):
        if (windows_sum_list[i] > windows_sum_list[i-1]):
            res += 1
    return res


# Unit test
assert part2(testReport) == 5
