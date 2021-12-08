
def prepare_data(file):
    """It prepare the fishes list"""
    with open(file) as file:
        data = file.read().splitlines()
        res = []
        for pattern in data:
            res_dict = {'signal_patterns': [], 'output_values': []}
            split_data = pattern.split(' | ')
            res_dict['signal_patterns'] = split_data[0].split()
            res_dict['output_values'] = split_data[1].split()
            res.append(res_dict)
    return res


def part1(data):
    res = 0
    for entry in data:
        for value in entry['output_values']:
            if len(value) in (2, 3, 4, 7):
                res += 1
    return 1

