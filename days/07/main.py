from crab import *


with open('input.txt') as file:
    crab_pos = file.readlines()
    crab_pos_list = [int(i) for i in crab_pos[0].split(',')]

    # print(part1(crab_pos_list)) # 341534
    assert part1(crab_pos_list) == 341534
    # print(part2(crab_pos_list)) # 93397632
    assert part2(crab_pos_list) == 93397632
