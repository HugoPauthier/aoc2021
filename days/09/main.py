from part_one import *

with open('input.txt') as file:
    input_data = file.read().splitlines()
    # print(input_heightmap)
    input_heightmap = prepare_data(input_data)
    # print(input_heightmap)
    # print(part1(input_heightmap))
    print(part2(input_heightmap))

# tested 254880
