from part_one import *

with open('test_input.txt') as file:
    test_nav_sub = file.read().splitlines()
    # print(part1(test_nav_sub))
    # assert part1(test_nav_sub) == 26397
    # print(part2(test_nav_sub))


with open('input.txt') as file:
    nav_dub = file.read().splitlines()
    # print(part1(nav_dub))
    # assert part1(nav_dub) == 464991
    print(part2(nav_dub))
