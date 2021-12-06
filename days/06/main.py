from lanternfish import *


def prepare_data(file):
    """It prepare the fishes list"""
    with open(file) as file:
        fishes = file.readlines()
        fishes_list = [int(i) for i in fishes[0].split(',')]
    return fishes_list


d0_fishes_list = prepare_data('input.txt')


print(part1(d0_fishes_list, 80))  # 355386
assert part1(d0_fishes_list, 80) == 355386

d0_fishes_dict = prepare_lists(d0_fishes_list)
print(part2(d0_fishes_dict, 256))
assert part2(d0_fishes_dict, 256) == 1613415325809
