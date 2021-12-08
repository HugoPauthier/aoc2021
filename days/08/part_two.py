
def prepare_data(file):
    """It prepare the data list"""
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


test_data = prepare_data('test_input.txt')

test_data2 = [{'signal_patterns': ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd',
                                   'cdfgeb', 'eafb', 'cagedb', 'ab'], 'output_values': ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']}]


def get_1478(signal_patterns):
    """
    Inits the mapped signal with obvious values
    Indeed, the digits 1, 4, 7, 7 are obvious to guess using the pattern length
    """
    res = {}
    for entry in signal_patterns:
        if len(entry) == 2:
            res['1'] = entry
        elif len(entry) == 3:
            res['7'] = entry
        elif len(entry) == 4:
            res['4'] = entry
        elif len(entry) == 7:
            res['8'] = entry
    return res


def get_common_char(str1, str2):
    set_str1 = set(str1)
    set_str2 = set(str2)
    common_char = set_str1 & set_str2
    return len(common_char)


assert get_common_char('fbcad', 'ab') == 2
assert get_common_char('ab', 'fbcad') == 2


#     aaaa
#    b    c
#    b    c
#     dddd
#    e    f
#    e    f
#     gggg
def map_signals(signal_patterns):
    """Matches the different signal patterns to the corresponding digit"""
    res = get_1478(signal_patterns)
    for entry in signal_patterns:
        if len(entry) == 5:
            # 2, 3, 5
            if get_common_char(entry, res['4']) == 3:
                if get_common_char(entry, res['1']) == 2:
                    res['3'] = entry
                else:
                    res['5'] = entry
            else:
                res['2'] = entry
        elif len(entry) == 6:
            # 0, 6, 9
            if get_common_char(entry, res['1']) == 2:
                if get_common_char(entry, res['4']) == 4:
                    res['9'] = entry
                else:
                    res['0'] = entry
            else:
                res['6'] = entry
    return res


def is_equal(str1, str2):
    """
    Return True if the two values contain the same char
    ie: 'cbef' equals 'efbc'
    """
    if len(str1) != len(str2):
        return False
    else:
        return(all(c in str2 for c in str1))


assert is_equal('cbef', 'bfec') is True
assert is_equal('cbef', 'bfxc') is False


def decode_output_value(output_values, mapped_signals):
    """Decodes the ouput value using the mapped signals"""
    res = ''
    for value in output_values:
        for key, val in mapped_signals.items():
            if is_equal(val, value):
                res += key
    return int(res)


def part2(data):
    """Part two"""
    res = 0
    for entry in data:
        # print('ENTRY', entry['signal_patterns'])
        mapped_signals = map_signals(entry['signal_patterns'])
        # print('Mapped signals:', mapped_signals)
        output_value = decode_output_value(
            entry['output_values'], mapped_signals)
        # print('Output value:', output_value)
        res += output_value
    return res


# print(part2(test_data)) # 61229
assert part2(test_data) == 61229
