from part1 import *

with open('test_input.txt') as file:
    test_data = file.read().splitlines()
    test_caves_map = prepare_data(test_data)
    print(test_caves_map)
    print(part1(test_caves_map))

with open('input.txt') as file:
    input_data = file.read().splitlines()
    input_caves_map = prepare_data(input_data)
    print(input_caves_map)
    print(part1(input_caves_map))