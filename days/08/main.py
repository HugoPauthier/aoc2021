from part_one import *
from part_two import *

test_data = prepare_data('test_input.txt')
data = prepare_data('input.txt')


# Part 1

print('Test part1:', part1(test_data))  # 26
assert part1(test_data) == 26

print('Result part1:', part1(data))  # 392
assert part1(data) == 392


# Part 2

print('Test part2:', part2(test_data))  # 61229
assert part2(test_data) == 61229

print('Result part2:', part2(data))  # 1004688
assert part2(data) == 1004688
