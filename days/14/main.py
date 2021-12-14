from part_one import *

test_template, test_pairs = prepare_data("test_input.txt")
test_polymer = part1(test_template, test_pairs, 10)

print(most_sub_least(test_polymer))
assert most_sub_least(test_polymer) == 1588


input_template, input_pairs = prepare_data("input.txt")
input_polymer = part1(input_template, input_pairs, 10)

print(most_sub_least(input_polymer))
assert most_sub_least(input_polymer) == 3230
