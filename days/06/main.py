from part_one import *

def prepare_data(file):
    """It prepare the fishes list"""
    with open(file) as file:
        fishes = file.readlines()
        fishes_list = [int(i) for i in fishes[0].split(',')]
    return fishes_list

d0_fishes_list = prepare_data('input.txt')
# d80_fishes = part1(d0_fishes_list, 80)
d256_fishes = part1(d0_fishes_list, 256)
# print(d80_fishes)