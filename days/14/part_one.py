def prepare_data(filename):
    """Gets the data from the specified file"""
    with open(filename) as file:
        data = file.read().splitlines()
        template = data[0]
        pairs = {}
        for i in range(2, len(data)):
            pairs_split = data[i].split(" -> ")
            pairs[pairs_split[0]] = pairs_split[1]
        return template, pairs


def most_sub_least(polymer):
    cnt = [polymer.count(c) for c in polymer]
    res = set(cnt)
    return max(res) - min(res)


assert most_sub_least("NNNNBBNCB") == 4


def part1(template, pairs, n_step):
    for n in range(n_step):
        tmp = template
        for i in range(0, len(tmp) - 1):
            curr_pair = tmp[i] + tmp[i + 1]
            match = pairs[curr_pair]
            template = template[: i * 2 + 1] + match + template[i * 2 + 1 :]
    return template
