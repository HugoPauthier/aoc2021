from bingo import part1, part2, prepare_data

(numbers, boards) = prepare_data('input.txt')
# print(part1(numbers, boards))
assert part1(numbers, boards) == 63424

(numbers, boards) = prepare_data('input.txt')
# print(part2(numbers, boards))
assert part2(numbers, boards) == 23541