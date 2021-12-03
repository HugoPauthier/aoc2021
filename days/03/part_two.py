test = ["00100", "11110", "10110", "10111", "10101", "01111",
        "00111", "11100", "10000", "11001", "00010", "01010"]


def get_oxy_gen_rat(report):
    """
    This function is used to calculate
    the oxygen generator rating from
    the diagnostic report
    """
    res = report.copy()
    for i in range(len(report[1])):
        bit_occ = {'0': [], '1': []}
        for number in res:
            if number[i] == "0":
                bit_occ['0'].append(number)
            elif number[i] == "1":
                bit_occ['1'].append(number)
        zeros = bit_occ["0"]
        ones = bit_occ["1"]
        if ((len(zeros) > 0) and (len(ones) > 0)):
            if len(ones) >= len(zeros):
                res = ones
            else:
                res = zeros
    return int(res[0], 2)


def get_co2_scrub_rat(report):
    """
    This function is used to calculate
    the CO2 scrubber rating from
    the diagnostic report
    """
    res = report.copy()
    for i in range(len(report[1])):
        bit_occ = {'0': [], '1': []}
        for number in res:
            if number[i] == "0":
                bit_occ['0'].append(number)
            elif number[i] == "1":
                bit_occ['1'].append(number)
        zeros = bit_occ["0"]
        ones = bit_occ["1"]
        if ((len(zeros) > 0) and (len(ones) > 0)):
            if len(ones) >= len(zeros):
                res = zeros
            else:
                res = ones
    return int(res[0], 2)


def part2(report):
    """Result function"""
    oxy_gen_rat = get_oxy_gen_rat(report)
    co2_scrub_rat = get_co2_scrub_rat(report)
    return oxy_gen_rat * co2_scrub_rat


# print(get_oxy_gen_rat(test))
# print(get_co2_scrub_rat(test))
assert get_oxy_gen_rat(test) == 23
assert get_co2_scrub_rat(test) == 10
assert part2(test) == 230
