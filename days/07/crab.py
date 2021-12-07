test = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def get_fuel(i, crab_pos):
    res = []
    for crab in crab_pos:
        res.append(abs(i - crab))
    return res


def get_min_fuel(fuel_list):
    res = []
    for i in range(len(fuel_list[0])):
        fuel_sum = 0
        for f in fuel_list:
            fuel_sum += f[i]
        res.append(fuel_sum)
    return min(res)


def sigma(n):
    res = 0
    for i in range(n + 1):
        res += i
    return res


def part1(crab_pos):
    fuel_sums = []
    for i in range(max(crab_pos)):
        fuel_list = []
        for crab in crab_pos:
            fuel_list.append(abs(crab - i))
        fuel_sums.append(sum(fuel_list))
    return min(fuel_sums)

# print(part1(test))


def part2(crab_pos):
    fuel_sums = []
    for i in range(max(crab_pos)):
        fuel_list = []
        for crab in crab_pos:
            fuel_list.append(sigma(abs(crab - i)))
        fuel_sums.append(sum(fuel_list))
    return min(fuel_sums)

# print(part2(test))
