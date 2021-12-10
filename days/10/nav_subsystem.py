char_pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
illegal_table = {')': 3, ']': 57, '}': 1197, '>': 25137}
completion_table = {')': 1, ']': 2, '}': 3, '>': 4}


def is_corrupted(line):
    open_chars = []
    res = ''
    for curr_char in line:
        if curr_char in ('(', '[', '{', '<'):
            open_chars.append(curr_char)
        else:
            if curr_char == char_pairs[open_chars[-1]]:
                open_chars.pop()
            else:
                res = curr_char
                return res, open_chars
    return res, open_chars


assert is_corrupted('{([(<{}[<>[]}>{[]{[(<()>') == ('}', [
    '{', '(', '[', '(', '<', '['])
assert is_corrupted('[{[{({}]{}}([{[{{{}}([]') == (']', [
    '[', '{', '[', '{', '('])


def part1(navigation_sub):
    res = 0
    for line in navigation_sub:
        illegal_char, open_chars = is_corrupted(line)
        if illegal_char != '':
            res += illegal_table[illegal_char]
    return res


def part2(navigation_sub):
    scores = []
    for line in navigation_sub:
        illegal_char, open_chars = is_corrupted(line)
        if illegal_char == '':
            res = 0
            for i in range(len(open_chars) - 1, -1, -1):
                # print(open_chars[i], char_pairs[open_chars[i]])
                res *= 5
                res += completion_table[char_pairs[open_chars[i]]]
            scores.append(res)
    scores.sort()
    return scores[len(scores)//2]
