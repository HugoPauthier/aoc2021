test = ["00100", "11110", "10110", "10111", "10101", "01111",
        "00111", "11100", "10000", "11001", "00010", "01010"]


def get_epsilon(gamma):
    """
    This function is used to calculate
    the epsilon rate from
    the gamma rate
    """
    epsilon = ''.join('1' if x == '0' else '0' for x in gamma)
    return epsilon


def get_gamma(report):
    """
    This function is used to calculate
    the gamma rate from
    the diagnostic report
    """
    gamma = ""
    for i in range(len(report[1])):
        bits = []
        for number in report:
            bits.append(number[i])
        gamma += get_max_occ(bits)
    return gamma


def get_max_occ(llist):
    """It gets the max occurence from an element in a list"""
    max_curr = 0
    num = llist[0]

    for i in llist:
        curr_frequency = llist.count(i)
        if curr_frequency > max_curr:
            max_curr = curr_frequency
            num = i

    return num


def part1(report):
    """Result function"""
    res_gamma = get_gamma(report)
    res_epsilon = get_epsilon(res_gamma)
    return int(res_gamma, 2) * int(res_epsilon, 2)


assert part1(test) == 198
