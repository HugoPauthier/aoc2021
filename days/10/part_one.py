char_pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
point_table = {')': 3, ']': 57, '}': 1197, '>': 25137}
completion_table = {')': 1, ']': 2, '}': 3, '>': 4}
# char_pairs = {')': '(', ']': '[', '}': '{', '>': '<'}


# def parse_line(line, i, close_char):
#     print('parsing i=', i, 'expecting=', close_char)
#     if line[i + 1] == close_char:
#         print('found closing char', close_char)
#         return 1
#     parse_line(line, i + 1, char_pairs[line[i + 1]])


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
                # print(f'expected {char_pairs[open_chars[-1]]} got {curr_char}')
                res = curr_char
                return res, open_chars
    return res, open_chars
    # res = parse_line(line, 0, char_pairs[line[0]])

# print(is_corrupted('{([(<{}[<>[]}>{[]{[(<()>'))
# print(is_corrupted('[{[{({}]{}}([{[{{{}}([]'))


def part1(navigation_sub):
    res = 0
    for line in navigation_sub:
        illegal_char, open_chars = is_corrupted(line)
        if illegal_char != '':
            res += point_table[illegal_char]
    return res

def part2(navigation_sub):
    scores = []
    for line in navigation_sub:
        illegal_char, open_chars = is_corrupted(line)
        if illegal_char == '':
            # print(open_chars)
            res = 0
            for i in range(len(open_chars) -1, -1, -1):
                # print(open_chars[i], char_pairs[open_chars[i]])
                res *= 5
                res += completion_table[char_pairs[open_chars[i]]]
            scores.append(res)
    scores.sort()
    print(scores[len(scores)//2])
    return 1
