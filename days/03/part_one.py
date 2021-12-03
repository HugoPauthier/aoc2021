test = ["00100", "11110", "10110", "10111", "10101", "01111",
        "00111", "11100", "10000", "11001", "00010", "01010"]


def getEpsilon(gamma):
    epsilon = ''.join('1' if x == '0' else '0' for x in gamma)
    return epsilon


def getGamma(report):
    gamma = ""
    for i in range(len(report[1])):
        bits = []
        for number in report:
            bits.append(number[i])
        gamma += getMaxOcc(bits)
    return gamma


def getMaxOcc(List):
    max_curr = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency > max_curr):
            max_curr = curr_frequency
            num = i

    return num


def part1(report):
    res_gamma = getGamma(report)
    res_epsilon = getEpsilon(res_gamma)
    return int(res_gamma, 2) * int(res_epsilon, 2)


assert part1(test) == 198
